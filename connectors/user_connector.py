import asyncio
import os
import datetime

from fastapi.websockets import WebSocket

from connectors.states import States
from models import GraphicMessage, LastMessage, AnalystData
from connectors.calculator import Calculator


class _FileReceiver:
    def __init__(self):
        self.__receiving = False
        self.__current_file: str | None = None
        self.__file_handle = None
        self.__file_extension = "mp4"
    
    async def start_receiving(self):
        os.makedirs("received_files", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.__current_file = f"received_files/video_{timestamp}.{self.__file_extension}"
        self.__file_handle = open(self.__current_file, "wb")
        self.__receiving = True
    
    async def receive_chunk(self, chunk: bytes):
        if not self.__receiving or not self.__file_handle:
            raise Exception("Not in receiving state")

        self.__file_handle.write(chunk)
        
    async def end_receiving(self):
        if not self.__receiving:
            return
        
        if self.__file_handle:
            self.__file_handle.close()

        self.__receiving = False
        self.__file_handle = None

    @property 
    def file_name(self):
        return self.__current_file
    

class UserConnector:
    def __init__(self, states: States):
        self.__current_socket: WebSocket | None = None
        self.__states = states
        self.__reciver = _FileReceiver()
        self.__calculator = Calculator()

    async def connect(self, socket: WebSocket):
        self.__current_socket = socket 
        await socket.accept()
        while True:
            answer = socket.receive_json()
            if answer is not None:
                if answer["type"] == "start_file_sennding":
                    self.__reciver.start_receiving()
                elif answer["type"] == "file":
                    self.__reciver.receive_chunk(bytes(answer["file_pice"]))
                elif answer["end_file_sending"]:
                    self.__reciver.end_receiving()
                    file = self.__reciver.file_name
                    await self.send_answers(file)
    
    async def send_answers(self, file_name: str):
        neural = self.__states.get_neural()
        last_data = None
        for data in await neural.send_file(file_name):
            last_data = data
            graphic = self.__calculator.calc_graphic()
            self.__current_socket.send_json(graphic.model_dump_json())
            asyncio.sleep(0.1)
        self.__current_socket.send_json(self.__calculator.calc_last(last_data).model_dump_json())
        

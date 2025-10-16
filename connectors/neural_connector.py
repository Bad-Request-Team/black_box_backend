import asyncio

from fastapi.websockets import WebSocket
import cv2

from models import AnalystData


class NeuralConnector:
    def __init__(self):
        self.__task_file: str | None = None
        self.__current_socket: WebSocket | None = None

    async def connect(self, socket: WebSocket):
        self.__current_socket = socket 
        await socket.accept()
        while True:
            await asyncio.sleep(60)

    async def send_file(self, task_file: str):
        self.__task_file = task_file
        video = cv2.VideoCapture(self.__task_file)
        count_frames = 0
        while True:
            ret, frame = video.read()
            byte_frame = frame.tobytes()
            data = {"frame": byte_frame, "frame_id": count_frames}
            await self.__current_socket.send_json(data)
            answer = await self.__current_socket.receive_json()
            if answer is not None:
                data = AnalystData.model_validate_json(answer)
                yield data

            if not ret:
                break
            await asyncio.sleep(0.1)
            count_frames += 1

        self.__task_file = None

import asyncio

from fastapi.websockets import WebSocket


class NeuralConnector:
    def __init__(self):
        self.__task_file: str | None = None

    async def connect(self, socket: WebSocket):
        await socket.accept()
        while self.__task_file is None:
            await asyncio.sleep(0.1)

    async def send_file(self, task_file: str):
        self.__task_file = task_file
        video = cv2.VideoCapture(self.__task_file)
        while True:
            pass
        self.__task_file = None

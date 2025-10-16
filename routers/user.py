from fastapi import APIRouter
from fastapi.websockets import WebSocket

import logging

from connectors import States, NeuralConnector, UserConnector

router = APIRouter()
states = States()

logger = logging.getLogger("NeuralConnector")


@router.websocket("/user_ws")
async def user_socket(socket: WebSocket):
    """Web scoket connect for user interface"""
    logger.info("user connected")
    user_connector = UserConnector(states)
    await user_connector.connect(socket)


@router.websocket("/neural_ws")
async def neural_socket(socket: WebSocket):
    """Web scoket connect for ssneural"""
    logger.info("neural connected")
    neural = NeuralConnector()
    await neural.connect(socket)
    async for i in neural.send_file("first_15_seconds.mp4"):
        print(i)
    states.add_neural(neural)

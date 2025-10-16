from fastapi import APIRouter
from fastapi.websockets import WebSocket

from connectors import States, NeuralConnector, UserConnector

router = APIRouter()
states = States()


@router.websocket("/user_ws")
async def user_socket(socket: WebSocket):
    """Web scoket connect for user interface"""
    user_connector = UserConnector(states)
    await user_connector.connect()


@router.websocket("/neural_ws")
async def neural_socket(socket: WebSocket):
    """Web scoket connect for neural"""
    neural = NeuralConnector()
    states.add_neural(neural)
    await neural.connect()

from fastapi import APIRouter
from fastapi.websockets import WebSocket

router = APIRouter(prefix="/neural_ws")


@router.websocket("/")
async def neural_socket(socket: WebSocket):
    """Web scoket connect for neural"""
    pass

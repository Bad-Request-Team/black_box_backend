from fastapi import APIRouter
from fastapi.websockets import WebSocket

router = APIRouter("/user_ws")


@router.websocket("/")
async def user_socket(socket: WebSocket):
    """Web scoket connect for user interface"""
    pass

from fastapi import APIRouter, WebSocket
from endpoints.api.v1.websocket.methods.connection_manager import ConnectionManager
import random
import string
from mongo import db

router = APIRouter()
manager = ConnectionManager()


@router.websocket('/{session_id}')
async def websocket_endpoint(websocket: WebSocket, session_id: str, authentication_token: str = None):
    await manager.connect(websocket)
    await websocket.send_json({'success': True})

    while True:
        data = await websocket.receive_json()
        await websocket.send_text(f'You said: {data}')

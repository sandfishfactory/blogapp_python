from datetime import datetime
import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/chat/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            record = json.loads(data)
            record["receive_timestamp"] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            print(record)
            await manager.broadcast(json.dumps(record))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(f"Client #{client_id} left the chat")
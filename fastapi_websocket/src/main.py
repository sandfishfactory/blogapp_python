import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles

from app.chat import router as chatRouter

app = FastAPI()
app.include_router(chatRouter)

app.mount("/", StaticFiles(directory="front/public"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI()


connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            # In this example, we send a message to all connected clients every second.
            await asyncio.sleep(1)
            message = "Streaming data..."
            for client in connected_clients:
                await client.send_text(message)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

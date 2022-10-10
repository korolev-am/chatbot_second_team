import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from core.proc import aiml
from core.load import loading
from core.processing import processing

import core.constants as const
app = FastAPI()

kernel = loading()
input_memory = []
ans = ''

origins = ['http://127.0.0.1:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json(const.MESSAGES[1])
    while True:
        data = await websocket.receive_text()
        global ans
        global input_memory
        ans, input_memory, message = processing(data, kernel, input_memory, False, ans)
        await websocket.send_json(message)
        while len(message['buttons']) == 0:
            if message['id'] == 100:  # НЕ ПОНИМАЮ ОТВЕТА
                pass
            else:
                ans, input_memory, message = processing(message['id'], kernel, input_memory, True, ans)
                await websocket.send_json(message)

def start():
    """
    Launched with 'poetry run start' at root level
    """
    uvicorn.run(
        app='app.app:app', 
        host='localhost', 
        port=9191, 
        reload=True,
        workers=1,
    )

import numbers
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from core.proc import aiml
from core.load import loading
from core.processing import processing

import core.constants as const
app = FastAPI()

with open('./docs/docs.html') as f:
    docs_file = f.read()

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
    kernel = loading()
    input_memory = []
    ans = ''
    last_message = 0
    await websocket.send_json(const.MESSAGES[1])
    while True:
        data = await websocket.receive_text()
        ans, input_memory, message = processing(data, kernel, input_memory, False, ans) # ответ пользователя
        if message['id'] != '100':
            last_message = message
        if message['id'] == '126':
            file = open("./user_questions.txt", "a")
            file.write(input_memory[-1] + '\n')
            file.close()
        await websocket.send_json(message)
        while len(message['buttons']) == 0:
            if message['id'] != '100':  # корректный запрос
                ans, input_memory, message = processing(message['id'], kernel, input_memory, True, ans) # наш ответ
                if message['id'] != '100':
                    last_message = message
                await websocket.send_json(message)
            else: # некорретный запрос
                print(last_message)
                await websocket.send_json(last_message)
                break

@app.get('/ws/docs')
async def method_for_docs():
    """
    Fetch docs for websocket here
    """
    return HTMLResponse(docs_file)

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

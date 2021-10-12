from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import json
from prediction import get_prediction
import pandas as pd

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    body = '''
        <h1>DPS Task API Endpoint Devansh Srivastav</h1>
        <p>Check the docs: <a href='/docs'> here</a></p>
    '''
    return HTMLResponse(content=body, status_code=200)


@app.post('/prediction')
async def get_result(year: str, month: str):
    return json.loads(get_prediction(year, month).to_json(orient='records'))[0]

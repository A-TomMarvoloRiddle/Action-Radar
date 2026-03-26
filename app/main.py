from fastapi import FastAPI
from pydantic import BaseModel
import json

import time 

from google.adk.runners import Runner
from app.agent import root_agent

app = FastAPI(title="ActionRadar API")

runner = Runner(root_agent)


class Request(BaseModel):
    meeting_text: str


@app.post("/analyze")
def analyze(req: Request):
    response = runner.run(input=req.meeting_text)

    try:
        return json.loads(response.output)
    except:
        return {
            "error": "Invalid JSON from model",
            "raw_output": response.output
        }

@app.get("/")
def root():
    return {
        "message": "ActionRadar API is live 🚀",
        "endpoint": "/analyze"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "actionradar",
        "version": "1.0",
        "uptime_seconds": round(time.time() - START_TIME, 2)
    }
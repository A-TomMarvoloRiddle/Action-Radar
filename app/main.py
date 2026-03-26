from fastapi import FastAPI
from pydantic import BaseModel
import json

from google.adk.runners import Runner
from app.agent import root_agent

app = FastAPI(title="ActionRadar API")

runner = Runner(root_agent)


class Request(BaseModel):
    meeting_text: str


@app.get("/")
def health():
    return {"status": "running"}


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
from fastapi import FastAPI, HTTPException

from app.schemas import RequestSchema, ResponseSchema
from app.agent import run_actionradar
from app.utils import safe_parse

app = FastAPI(title="ActionRadar API")


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/analyze", response_model=ResponseSchema)
def analyze(request: RequestSchema):
    try:
        raw_output = run_actionradar(request.meeting_text)

        parsed = safe_parse(raw_output)

        return parsed

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from pydantic import BaseModel, Field
from typing import List


class ActionItem(BaseModel):
    task: str = Field(..., description="Actionable task")
    owner: str = Field(..., description="Responsible person")
    deadline: str = Field(..., description="YYYY-MM-DD or 'Not specified'")
    priority: float = Field(..., ge=0, le=1)


class ResponseSchema(BaseModel):
    action_items: List[ActionItem]
    blockers: List[str]
    summary: str
    confidence: float = Field(..., ge=0, le=1)


class RequestSchema(BaseModel):
    meeting_text: str
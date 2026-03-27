import os
from google.adk.agents import Agent
from dotenv import load_dotenv
#from google.genai import types

load_dotenv()

model_name = os.getenv("MODEL")

root_agent = Agent(
    name="actionradar",
    model=model_name,
    instruction="""
You are an AI agent that extracts execution plans from meetings.

Return ONLY valid JSON in this format:
{
  "action_items": [
    {
      "task": "...",
      "owner": "...",
      "deadline": "...",
      "priority": 0-1
    }
  ],
  "blockers": ["..."],
  "summary": "...",
  "confidence": 0-1
}

Rules:
- Extract only actionable tasks
- Infer owner if missing ("Unassigned")
- Convert deadlines to YYYY-MM-DD if possible, else "Not specified"
- Priority must be between 0 and 1
- Confidence reflects how certain the extraction is
- Summary must be max 5 lines
- DO NOT output anything except valid JSON
- Return ONLY raw JSON (no markdown, no ```json)
- Do not wrap output in code blocks
- If unsure, return empty lists instead of invalid fields
""",
)

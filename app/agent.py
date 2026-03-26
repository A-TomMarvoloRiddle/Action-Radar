import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.models import Gemini

from app.prompt import SYSTEM_PROMPT

from google.genai import types

load_dotenv()

# Initialize Gemini via ADK
model = Gemini(model="gemini-2.5-flash")

# Define ADK Agent
agent = Agent(
    name="actionradar",
    model=model,
    retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2),
    instruction=SYSTEM_PROMPT,
)

# Runner to execute agent
runner = Runner(agent)


def run_actionradar(meeting_text: str) -> str:
    response = runner.run(
        input=meeting_text
    )
    return response.output
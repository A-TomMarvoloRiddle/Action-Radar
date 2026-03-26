import os

from google.adk.agents import Agent

from app.prompt import SYSTEM_PROMPT

from google.genai import types

root_agent = Agent(
    name="actionradar",
    model="gemini-2.5-flash",
    retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2),
     description="Extract structured execution plans from meeting transcripts.",
    instruction=SYSTEM_PROMPT,
)

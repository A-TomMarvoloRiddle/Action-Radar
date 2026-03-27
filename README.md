# ActionRadar

ActionRadar is a single ADK-powered AI agent that transforms meeting transcripts into a structured execution plan.

It extracts:
- action items
- owners
- deadlines
- blockers
- a short summary
- a confidence score

The project is deployed on Google Cloud Run and exposed through the ADK HTTP interface.

## Why ActionRadar stands out

Instead of just summarizing a meeting, ActionRadar turns discussion into an execution-ready output. It highlights:
- who is responsible
- what needs to be done
- when it should be completed
- what is blocking progress

This makes it more useful than a basic summarizer or classifier while still staying within the single-agent scope of the hackathon.

## Tech Stack

- Google ADK
- Gemini 2.5 Flash
- Google Cloud Run
- Python

## Project Structure

```text
actionradar/
├── agent.py
├── __init__.py
├── requirements.txt
├── README.md
└── .env
```

## Agent Behavior

The agent accepts a meeting transcript as input and returns only valid JSON in this format:

```json
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
  "summary": "..."
}
```

### Output Rules

- `action_items` should contain every clear task discussed in the transcript.
- `owner` should be inferred when possible; use `Unassigned` if unclear.
- `deadline` should be written clearly YYYY-MM-DD; use `Not specified` if none is mentioned.
- `priority` should be a number between `0` and `1`.
- `blockers` should contain all blockers mentioned in the transcript.
- `summary` should be short and limited to a maximum of 5 lines.
- DO NOT output anything except valid JSON
- Return ONLY raw JSON (no markdown, no ```json)
- Do not wrap output in code blocks
- If unsure, return empty lists instead of invalid fields

## Local Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set environment variables

Create a `.env` file with the required Google Cloud / Vertex AI settings used by ADK:

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=asia-south1
```

### 4. Run locally with ADK

From inside the project folder:

```bash
adk web .
```

## Deploy to Cloud Run

Deploy the agent directly with ADK:

```bash
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name actionradar \
  --with_ui \
  .
```

## Usage

After deployment, open the Cloud Run URL in a browser.

You can paste a meeting transcript directly into the UI and receive the final structured JSON response.

### Example Input

```text
Alright, let's get started. So first thing — the UI for the dashboard is still pending. Rahul, I think you were supposed to finalize that?

Yeah, I’ve done most of it, just need to finish the analytics section. I can get that done by Friday.
```

### Example Output

```json
{
  "action_items": [
    {
      "task": "Finish the analytics section of the dashboard UI",
      "owner": "Rahul",
      "deadline": "Friday",
      "priority": 0.86
    }
  ],
  "blockers": [
    "Waiting on backend APIs"
  ],
  "summary": "The team aligned on the remaining UI work, backend dependency, testing, deployment, and documentation tasks. The main blocker is the delayed backend API availability.",
}
```

## Notes for Reviewers

- This project intentionally focuses on a single, clearly defined task.
- It uses ADK for the agent structure.
- It uses Gemini 2.5 Flash for inference.
- It is deployed on Cloud Run and can be accessed through the provided service URL.
- The output is designed to be directly usable as an execution plan.


# ActionRadar 🚀

AI Agent that converts meeting transcripts into structured execution plans.

## 🔥 Features
- Extracts action items
- Assigns owners
- Detects blockers
- Generates priority scores
- Confidence scoring

## 🧠 Tech Stack
- Google ADK (Agent Development Kit)
- Gemini 2.5 Flash
- FastAPI
- Docker
- Google Cloud Run

## 📡 API

### POST /analyze

#### Input
{
  "meeting_text": "Rahul will finish UI by Friday. Waiting for backend API."
}

#### Output
{
  "action_items": [
    {
      "task": "Finish UI",
      "owner": "Rahul",
      "deadline": "2026-03-28",
      "priority": 0.9
    }
  ],
  "blockers": ["Waiting for backend API"],
  "summary": "UI completion depends on backend API.",
  "confidence": 0.87
}

## 🚀 Deployment

Deployed on Google Cloud Run.

## 📌 Note
This project strictly follows:
- Single AI agent
- ADK implementation
- Gemini inference
- HTTP endpoint exposure
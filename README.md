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

## API Endpoint

curl -X POST "https://actionradar-xxxxx.run.app/sessions" \
-H "Content-Type: application/json" \
-d '{
  "app_name": "actionradar",
  "user_id": "test_user",
  "session_id": "s1"
}'

curl -X POST "https://actionradar-xxxxx.run.app/run" \
-H "Content-Type: application/json" \
-d '{
  "app_name": "actionradar",
  "user_id": "test_user",
  "session_id": "s1",
  "new_message": {
    "role": "user",
    "parts": [
      {
        "text": "Rahul will complete UI by Friday. Waiting for backend API."
      }
    ]
  }
}'

This agent is deployed using Google ADK.

#### Input
{
  "app_name": "actionradar",
  "user_id": "demo_user",
  "session_id": "session_1",
  "new_message": {
    "role": "user",
    "parts": [
      {
        "text": "Your meeting transcript here"
      }
    ]
  }
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

## 📌 Note
This project strictly follows:
- Single AI agent
- ADK implementation
- Gemini inference
- HTTP endpoint exposure
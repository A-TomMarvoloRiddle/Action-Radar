import json

def safe_parse(output: str):
    try:
        return json.loads(output)
    except Exception:
        return {
            "action_items": [],
            "blockers": [],
            "summary": "Failed to parse structured output",
            "confidence": 0.0,
            "raw_output": output
        }
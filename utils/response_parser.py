import json

def parse_json_response(text):
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        return {"raw_response": text.strip()}
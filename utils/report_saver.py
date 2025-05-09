# utils/report_saver.py
import json
import os

def save_report(data, filename="data/reports/report.json"):
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\n📄 Report saved to {filename}")

def parse_json_response(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"raw_response": text}
    

    
import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError:
        return False

def validate_cve_data(cve_data):
    required_keys = ["summary", "cvss_score", "published_date"]
    for key in required_keys:
        if key not in cve_data:
            raise ValueError(f"Missing required CVE field: {key}")
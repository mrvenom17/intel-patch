import logging
import json

def pretty_print_json(text):
    try:
        parsed = json.loads(text)
        print(json.dumps(parsed, indent=2))
    except json.JSONDecodeError:
        print(text)

def setup_logger(name="intel-patch", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
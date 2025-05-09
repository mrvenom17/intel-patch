import logging
from utils.logger import setup_logger

logger = setup_logger()

def print_text_animated(text, delay=0.01):
    """Print text character-by-character for demo effect"""
    from time import sleep
    for char in text:
        print(char, end="", flush=True)
        sleep(delay)
    print("\n")

def load_prompt(prompt_name):
    import yaml
    try:
        with open("config/prompts.yaml") as f:
            prompts = yaml.safe_load(f)
        prompt = prompts.get(prompt_name)
        if not prompt:
            logger.warning(f"Prompt '{prompt_name}' not found in config.")
            return ""
        return prompt
    except Exception as e:
        logger.error(f"Failed to load prompt: {e}")
        return ""
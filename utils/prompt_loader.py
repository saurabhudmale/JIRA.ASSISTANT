import os

def load_prompt(prompt_name: str) -> str:
    prompt_path = os.path.join("prompts", prompt_name)
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()

def format_prompt(template: str, context: dict) -> str:
    return template.format(**context)

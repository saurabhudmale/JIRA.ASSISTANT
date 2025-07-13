from gpt_logic.gpt import gpt_request
from utils.prompt_loader import format_prompt, load_prompt

def convert_to_html(data):
    template = load_prompt("html_generator_prompt.txt")

    context = {
        "data": data
    }

    prompt = format_prompt(template, context)
    
    return gpt_request(prompt)
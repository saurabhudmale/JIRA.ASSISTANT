from gpt_logic.gpt import gpt_request
from utils.prompt_loader import format_prompt, load_prompt

def generate_test_cases(title, description):

    template = load_prompt("test_cases_generator_prompt.txt")

    context = {
        "title": title,
        "description": description
    }

    prompt = format_prompt(template, context)
    
    return gpt_request(prompt)

def generate_jql(user_input):

    template = load_prompt("jql_generator_prompt.txt")

    context = {
        "user_input": user_input
    }

    prompt = format_prompt(template, context)
    
    return gpt_request(prompt)
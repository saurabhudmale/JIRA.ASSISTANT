import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def gpt_request(prompt):
    try:
        client = Groq(
            api_key=os.getenv('GROQ_API_KEY'),
        )
            
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
from openai import OpenAI
from config.settings import OPENAI_API_KEY, NOVA_SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def get_response(user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=1024,
        messages=[
            {"role": "system", "content": NOVA_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
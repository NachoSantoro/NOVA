from openai import OpenAI
from config.settings import OPENAI_API_KEY, NOVA_SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

conversation_history = []

def get_response(user_message: str) -> str:
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=1024,
        messages=[
            {"role": "system", "content": NOVA_SYSTEM_PROMPT}
        ] + conversation_history
    )

    nova_response = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": nova_response
    })

    return nova_response
from openai import OpenAI
from config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

commands = {}

def register(intent: str, handler):
    commands[intent] = handler

def detect_intent(user_input: str) -> str:
    intents = list(commands.keys()) + ["conversation"]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=20,
        messages=[
            {
                "role": "system",
                "content": f"Clasificá la intención del usuario en exactamente una de estas opciones: {', '.join(intents)}. Respondé solo con la palabra, sin puntuación ni explicación."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    
    return response.choices[0].message.content.strip().lower()

def route(user_input: str):
    intent = detect_intent(user_input)
    print(f"[intent: {intent}]")
    
    if intent in commands:
        return commands[intent]()
    return None
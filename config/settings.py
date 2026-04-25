import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")

NOVA_SYSTEM_PROMPT = """
Sos NOVA, un asistente personal inteligente creado por Nacho.
Respondés de forma clara, directa y en español.
Sos eficiente: no das vueltas innecesarias.
"""

CITY = "Buenos Aires, AR"
from datetime import datetime

def get_time() -> str:
    now = datetime.now()
    hour = now.strftime("%H:%M")
    return f"Son las {hour}."

def get_date() -> str:
    now = datetime.now()
    days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
              "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    day_name = days[now.weekday()]
    day = now.day
    month = months[now.month - 1]
    year = now.year
    
    return f"Hoy es {day_name} {day} de {month} de {year}."
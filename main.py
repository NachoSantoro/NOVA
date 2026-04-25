from core.responder import get_response
from core.speaker import speak
from core.listener import listen
from core.router import register, route
from modules.weather import get_weather
from modules.clock import get_time, get_date

def main():
    register("weather", get_weather)
    register("time", get_time)
    register("date", get_date)

    print("NOVA iniciada. Decí 'salir' para terminar.\n")
    speak("NOVA iniciada. Te escucho.")
    
    while True:
        user_input = listen()
        
        if not user_input:
            continue
        
        if "salir" in user_input.lower():
            speak("Hasta luego.")
            print("NOVA: Hasta luego.")
            break

        response = route(user_input) or get_response(user_input)
        
        print(f"NOVA: {response}\n")
        speak(response)

if __name__ == "__main__":
    main()
from core.responder import get_response
from core.speaker import speak
from core.listener import listen

def main():
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
        
        response = get_response(user_input)
        print(f"NOVA: {response}\n")
        speak(response)

if __name__ == "__main__":
    main()
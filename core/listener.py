import speech_recognition as sr

recognizer = sr.Recognizer()

def listen() -> str:
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="es-AR")
        print(f"Vos: {text}")
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Error: no se pudo conectar al servicio de reconocimiento de voz.")
        return ""
from core.responder import get_response

def main():
    print("NOVA iniciada. Escribí 'salir' para terminar.\n")
    
    while True:
        user_input = input("Vos: ").strip()
        
        if user_input.lower() == "salir":
            print("NOVA: Hasta luego.")
            break
        
        if not user_input:
            continue
        
        response = get_response(user_input)
        print(f"NOVA: {response}\n")

if __name__ == "__main__":
    main()
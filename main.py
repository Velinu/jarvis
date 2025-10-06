from dotenv import load_dotenv
from bot import assistant
import os
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError(
        "It was not possible to "
        "Defina-a no .env ou exporte no terminal."
    )


def main():
    print("=== Assistente LangChain + Gemini ===")
    print("Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o assistente...")
            break

        try:
            response = assistant.run(user_input)
            print(f"Bot: {response}\n")
        except Exception as e:
            print(f"Erro ao processar sua mensagem: {e}\n")


if __name__ == "__main__":
    main()

import sys
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from gem_prompts import send_prompt_to_gemini

def get_bot_response(user_input):
    '''
    returns prompts ig
    '''
    return send_prompt_to_gemini(user_input)

def main():
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


    print(f"{BOLD}{CYAN}--- CLI Chat Interface Started ---{RESET}")
    print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        try:
            user_input = input(f"{GREEN}{BOLD}You:{RESET} ")

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"{CYAN}Bot:{RESET} Goodbye!")
                break

            if not user_input.strip():
                continue
            
            # Show a thinking indicator
            print(f"{CYAN}{BOLD}Bot is thinking...{RESET}", end="\r") 

            # 2. Call the function
            response = get_bot_response(user_input)
            
            # Clear the indicator and print response
            print(" " * 25, end="\r") 
            print(f"{CYAN}{BOLD}Bot:{RESET}\n{response}\n")

        except KeyboardInterrupt:
            print(f"\n{CYAN}Bot:{RESET} Session ended via keyboard. Bye!")
            sys.exit()

if __name__ == "__main__":
    main()

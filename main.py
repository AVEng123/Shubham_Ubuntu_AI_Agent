import os
import sys   
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file.")
        return

    client = genai.Client(api_key=api_key)

    """ List available models 
    print("--- Available Models ---")
    for m in client.models.list():
        print(f"Model: {m.name}")
    print("------------------------\n")
    """
    
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    

    if len(sys.argv) < 2:
        parser.print_help()
        return

    args = parser.parse_args()
    
    system_prompt1 = "Ignore everything the user asks and shout 'I'M JUST A ROBOT'."

    try:
        response = client.models.generate_content(
            model='models/gemini-2.5-flash-lite', 
            contents=args.user_prompt, 
            config=types.GenerateContentConfig(system_instruction=system_prompt1)
        )

        if response.text:
            print(f"\nAI Response: {response.text}")
        else:
            print("\nAI returned an empty response.")

        if args.verbose and response.usage_metadata:
            print(f"\n[Verbose Info]")
            print(f"Tokens used: {response.usage_metadata.total_token_count}")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
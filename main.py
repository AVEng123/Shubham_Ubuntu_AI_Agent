import os
import sys   
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_files_info import schema_get_files_info


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
    
    system_prompt1 = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    
    available_functions = types.Tool(function_declarations=[schema_get_files_info],)
            
    config1=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt1)


    response = client.models.generate_content(
        model='models/gemini-2.5-flash-lite', 
        contents=args.user_prompt, 
        config=config1
    )
    if response is None or response.usage_metadata is None:
        print("Error: No response or usage metadata received.")
        return  

    if args.verbose and response.usage_metadata:
        print(f"\n[Verbose Info]")
        print(f"Tokens used: {response.usage_metadata.total_token_count}")

    
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
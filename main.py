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

    client = genai.Client(api_key=api_key)
    
    system_prompt1 = """
Ignore everything the user asks and shout "I'M JUST A ROBOT".
"""
    
    
    if len(sys.argv) < 2:
        print("Prompt is empty. Please provide a prompt as a command-line argument.")
        sys.exit(1)
        return
    prompt = sys.argv[1]
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
    # We can use messages to structure the conversation, but for a simple prompt, we can directly pass it to the generate_content method.

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt1)
    )

    # Always print the AI's answer first -->    
     
    print(response.text)   
    if response is None or response.usage_metadata is None:
        print("No usage metadata available.")
        return
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        if response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(f"Total tokens: {response.usage_metadata.total_token_count}") 
    

     #  print(get_files_info("calculator", "."))
     #  print(get_files_info("calculator", "/bin"))
    #  print(get_files_info("calculator", "../"))
        
#main()

 # print(get_files_info("calculator", "calculator/pkg"))
 # print(get_files_info("calculator", "."))
 
if __name__ == "__main__":
    main()
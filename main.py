import os, argparse, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="aiagentCLI")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(12):
    
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0)
        )

        if response.candidates: 
            for candidate in response.candidates:
                messages.append(candidate.content)

        function_call_results_list = []
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            if response.usage_metadata is None:
                raise RuntimeError("Response usage metadata is None. API call failed.")
            else:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.thoughts_token_count}")
        if response.function_calls:
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)
                if not function_call_result.parts:
                    print("No response parts from function call.")
                else:
                    if not function_call_result.parts[0]:
                        print(f"Error calling function {function_call.name}: {function_call_result.parts[0].response['error']}")
                    if not function_call_result.parts[0].function_response:
                        raise Exception(f"No response from function {function_call.name}.")
                    function_call_results_list.append(function_call_result.parts[0])
                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
        else:
            print(response.text)
            return
        messages.append(types.Content(role="user", parts=function_call_results_list))

    if not response.text:
        print("No final response from model after 12 cycles.")
        sys.exit(1)


if __name__ == "__main__":
    main()
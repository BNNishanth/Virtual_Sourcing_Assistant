print(">>>agent.py loaded")

from huggingface_hub import InferenceClient
from assistant.prompt_templates import get_prompt

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    token="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"  # Replace with your token
)

def query_agent(user_input):
    print(">>>inside query_agent()")
    prompt = get_prompt(user_input)
    print(f"\nPrompt:\n{prompt}\n")
    
    result = client.text_generation(
        prompt=prompt,
        max_new_tokens=200,
        temperature=0.7,
        top_p=0.95,
        stream=False  # Make sure it's NOT streamed
    )
    
    print(f"\nRaw Result:\n{result}\n")
    return result
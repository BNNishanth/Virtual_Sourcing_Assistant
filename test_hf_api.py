from huggingface_hub import InferenceClient

# Replace this with your actual Hugging Face token
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    token=""
)

prompt = "You are a helpful assistant. How can a sourcing manager reduce RFQ negotiation time?"

response = client.text_generation(
    prompt=prompt,
    max_new_tokens=100,
    temperature=0.7,
    top_p=0.95
)

print("\nResponse:\n")
print(response)

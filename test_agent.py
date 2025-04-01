print(">>> Running test_agent.py")

from assistant.agent import query_agent

print(">>> Imported query_agent")

# No _main_ block yet — force it to run
user_input = "What are some sourcing cost-saving ideas?"
print(">>> Calling query_agent...")
response = query_agent(user_input)

print("\nAssistant's Response:\n")
print(response)

# Below code Generates a natural language instruction to the LLM 
# Wraps the user's question in context: “You're a sourcing assistant...”
# Keeps it flexible for many types of questions


def get_prompt(user_input):
    print(">>> Generating prompt...")  # Add this
    return f"You are a helpful sourcing assistant. {user_input}"
"""
You are a sourcing assistant helping a sourcing manager.

The user asked: "{user_input}"

Based on past RFQs and supplier profiles, respond helpfully.
Give suggestions or answer clearly.
"""

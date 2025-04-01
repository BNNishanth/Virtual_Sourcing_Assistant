import streamlit as st
from assistant.agent import query_agent

st.set_page_config(page_title="Sourcing Assistant", layout="centered", page_icon="🤖")

st.title("Virtual Sourcing Assistant")
st.write("Ask questions about RFQs, suppliers, or sourcing strategy.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = query_agent(user_input)
        st.session_state.chat_history.append((user_input, response))

# Display response
if st.session_state.chat_history:
    st.markdown("## Chat History")
    for i, (q, a) in enumerate(reversed(st.session_state.chat_history[-5:])):
        st.markdown(f"*Q{i+1}:* {q}")
        st.markdown(f"*A{i+1}:* {a}")
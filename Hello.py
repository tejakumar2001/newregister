import streamlit as st

def chatbot_response(input_text):
    # Define some simple rules or patterns for generating responses
    if "hello" in input_text.lower():
        return "Hi there! How can I help you?"
    elif "how are you" in input_text.lower():
        return "I'm doing well, thank you for asking!"
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    st.title("💬 Simple Chatbot")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for msg in st.session_state.messages:
        st.write(msg["role"], msg["content"])

    input_text = st.text_input("You", key="user_input")

    if input_text:
        response = chatbot_response(input_text)
        st.session_state.messages.append({"role": "user", "content": input_text})
        st.write("user", input_text)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write("assistant", response)

if __name__ == "__main__":
    main()

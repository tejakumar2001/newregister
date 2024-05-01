import streamlit as st
from openai import Client

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
    st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)")
    st.markdown("[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)")

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.write(msg["role"], msg["content"])

if prompt := st.text_input("You", key="user_input"):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = Client(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.write("user", prompt)
    response = client.complete(prompt, engine="text-davinci", stop="\n", temperature=0.5, max_tokens=100)
    msg = response.choices[0].text.strip()
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.write("assistant", msg)


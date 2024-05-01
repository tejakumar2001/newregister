import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "sk-proj-ueC2uxz6gQWMlJ6VHQ1uT3BlbkFJtkfFcgMgRk5fjAbqeI91"

def get_ai_response(question):
    # Use OpenAI's GPT-3 model to generate a response to the question
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    st.title("Generative AI Q&A")

    # User input for the question
    question = st.text_input("Ask a question")

    # Generate response when the user submits the question
    if st.button("Submit"):
        if not question:
            st.warning("Please enter a question.")
        else:
            response = get_ai_response(question)
            st.write("AI Answer:", response)

if __name__ == "__main__":
    main()



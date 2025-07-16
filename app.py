import streamlit as st
from qa_data import qa_dict

st.title("Kepler College Q&A Chatbot")

user_question = st.text_input("Ask a question about Kepler College:")

if user_question:
    # Simple exact match
    answer = qa_dict.get(user_question.strip())
    if answer:
        st.markdown(f"**Answer:** {answer}")
    else:
        st.markdown("Sorry, I don't have an answer for that. Please try another question.")

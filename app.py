import streamlit as st
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="Advanced Assistant")
st.title("🔥 Advanced Personal Assistant")

# Initialize model
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,)

# Initialize session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Prompt template with memory
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intelligent AI assistant. Give detailed, clear and structured answers."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

chain = prompt | model

# Chat input
user_input = st.chat_input("Ask anything...")

if user_input:
    # Add user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Invoke model
    response = chain.invoke({
        "input": user_input,
        "chat_history": st.session_state.chat_history
    })

    # Add AI response
    st.session_state.chat_history.append(AIMessage(content=response.content))

# Display chat
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    else:
        with st.chat_message("assistant"):
            st.write(message.content)
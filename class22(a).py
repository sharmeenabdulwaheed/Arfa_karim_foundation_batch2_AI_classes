import os
import streamlit as st
from groq import Groq
#!pip install groq

api="put_your_api"
st.title("💬Chat with Groq's Llama bot")

client= Groq(api_key=api)

#initialize empty list for history
if "history" not in st.session_state:
    st.session_state.history=[]


st.sidebar.title("Model Options for llama")
models=[]
model=st.sidebar.selectbox("Choose the model you want: ", ["llama3-8b-8192", "llama3-70b-8192"])

user_input=st.text_input("Enter your query: ")
if st.button("Submit"):
    chat=client.chat.completions.create(messages=[
        {
            "role":"user", 
            "content":user_input
        }
    ], model=model)
    response=chat.choices[0].message.content
    st.write(response)
    st.session_state.history.append({"query" : user_input, "response" : response})
##displaying history
st.sidebar.title("History")
for i,data in enumerate(st.session_state.history):
    if st.sidebar.button("Query: "+ data["query"]):
        st.write("Response: " +data["response"])
    





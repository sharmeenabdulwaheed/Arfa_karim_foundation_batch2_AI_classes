import os
import streamlit as st
from groq import Groq
import numpy as np
import pickle

api="put_your_api"
client= Groq(api_key=api)

st.title("Iris-specie Prediction App")
st.write("Please enter the data of flowers and ill predict its specie for you..")

sepal_l=st.number_input("Sepal Length: ",min_value= 0.0 )
sepal_w=st.number_input("Sepal width: ",min_value= 0.0 )
petal_l=st.number_input("Petal Length: ",min_value= 0.0 )
petal_w=st.number_input("Petal Width : ",min_value= 0.0 )

user_data=np.array([[sepal_l,sepal_w,petal_l,petal_w]])

#model load for prediction
with open("model.pkl", "rb") as file:
    model=pickle.load(file)

#model.predict
if st.button("Predict"):
    pred=model.predict(user_data)
    st.write("The prediction specie is", pred[0])

st.sidebar.title("Chatbot Settings")
enable=st.sidebar.checkbox("Enable chatting with a bot")
if enable:
    st.sidebar.title("Model Options for llama")
    model=st.sidebar.selectbox("Choose the model you want: ", ["llama3-8b-8192", "llama3-70b-8192"])
    user_input=st.text_input("Enter your query: ")
    if st.button("submit"):
        data=client.chat.completions.create(messages=[{"role":"user", "content": user_input}], model=model)
        response=data.choices[0].message.content
        st.write(response)
                                           







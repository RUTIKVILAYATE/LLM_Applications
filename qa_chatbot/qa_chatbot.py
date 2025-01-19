from dotenv import load_dotenv
load_dotenv()     ## loading all the environment variables


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSES
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])



def get_gemini_response(question):
        response = chat.send_message(question,stream=True)
        return response.text 


# INITIALIZE OUR STREAMLIT APP
st.set_page_config(page_title="QANDA DEMO")
st.header("Gemini LLM Application")

# INITIALIZE SESSION STATE FOR CHAT HISTORY IF IT DOESN'T EXIST
if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    # add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is") 
    for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The Chat History is")


for role,text in st.session_state['chat_history']:
       st.write(f"{role}:{text}")

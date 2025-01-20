from dotenv import load_dotenv
load_dotenv()     ## loading all the environment variables


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSES
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text 


# INITIALIZE OUR STREAMLIT APP
st.set_page_config(page_title="GEMINI IMAGE DEMO")
st.header("Gemini LLM Image Application")
input = st.text_input("Input Prompt: ",key="input")
submit = st.button("Ask the question")


#  When submit is clicked

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Upload Image", use_column_width=True) 


submit = st.button("Tell me about the image")

# if submit is clicked 
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is ")
    st.write(response)
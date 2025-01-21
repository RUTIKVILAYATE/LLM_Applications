# END TO END RESUME APPLICATION TRACKING SYSTEM 
# USING GEMINI PRO VISION


# IMPLEMENTATION 
# FIELD TO PUT MY JOB DESCRIPTION
# UPLOAD PDF OF RESUME 
# PDF TO IMAGE -> PROCESSING -> GOOGLE GEMINI PRO
# PROMPTS TEMPLATE (MULTIPLE PROMPTS)

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import base64
import os 
import io
from PIL import Image
import pdf2image     # needs to download -> poppler-windows
import google.generativeai as genai



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the pdf to image
        images = pdf2image.covert_from_bytes(uploaded_file.read())

        first_page = images[0]


        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr,format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()
        

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()       # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file Uploaded")
    

# Streamlit App

st.set_page_config(page_title= "ATS RESUME EXPERT")
st.header("ATS TRACKING SYSTEM")
input_text = st.text_area("Job Description: ",key="input") 
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])


if uploaded_file is not None:
    st.write("PDF uploadeded Successfully")

submit1 = st.button("Tell me About the Resume")
submit2 = st.button("How can I Improvise my skills")
submit3 = st.button("Percentage Match")



input_prompt1 = """
You are an experience Technical HR with Tech Experience in the field of any one job role from Data Science, Full Stack Web Development, 
Big Data Engineering, DEVOPS, Data Analyst, your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with highlight
the strength and weakness of the applicant in relation to the specified job descriptions """


input_prompt3 = """
You are an skilled ATS (Application Tracking System) scanner with a deep understanding of any one job role from Data Science, Full Stack Web Development, 
Big Data Engineering, DEVOPS, Data Analyst, and Deep ATS functionality, description for these profiles.
Your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume 
matches the job description. First the output should come as percentage and then keywords missing and last final thoughts"""



if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
    else:
        st.write("Please upload the resume")


elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
    else:
        st.write("Please upload the resume")

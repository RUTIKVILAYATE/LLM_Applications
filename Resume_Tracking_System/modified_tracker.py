from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import google.generativeai as genai
import PyPDF as pdf 
import os 



# import base64
# import io
# from PIL import Image
# import pdf2image     # needs to download -> poppler-windows



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro Response
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input])
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = " "
    for page in reader(len(reader.pages)):
        page = reader.pages[page]
        text+= str(page.extract_text())
    return text


input_prompt = """
You are an experience Technical HR with Tech Experience in the field of any one job role from Data Science, Full Stack Web Development, 
Big Data Engineering, DEVOPS, Data Analyst, your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with highlight
the strength and weakness of the applicant in relation to the specified job descriptions 
resume:{text}
description:{jd}

I want the response in one single string having the structure 
{{"JD Match": "%", "MissingKeywords:[]", "Profile Summary":"" }}


"""

# Streamlit App

st.title("Smart ATS")
st.set_page_config(page_title= "ATS RESUME EXPERT")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
st.header("ATS TRACKING SYSTEM")
input_text = st.text_area("Job Description: ",key="input") 
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"],help= "Please upload the pdf")


submit = st.button("Submit")
 
if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)

# if uploaded_file is not None:
#     st.write("PDF uploadeded Successfully")

# submit1 = st.button("Tell me About the Resume")
# submit2 = st.button("How can I Improvise my skills")
# submit3 = st.button("Percentage Match")







# input_prompt3 = """
# You are an skilled ATS (Application Tracking System) scanner with a deep understanding of any one job role from Data Science, Full Stack Web Development, 
# Big Data Engineering, DEVOPS, Data Analyst, and Deep ATS functionality, description for these profiles.
# Your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume 
# matches the job description. First the output should come as percentage and then keywords missing and last final thoughts"""



# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The Response is")
#     else:
#         st.write("Please upload the resume")


# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The Response is")
#     else:
#         st.write("Please upload the resume")

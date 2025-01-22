from dotenv import load_dotenv
load_dotenv() # load all the enviroment variables



import streamlit as st
import os 
import sqlite3


import google.generativeai as genai

# Configure the api key
genai.config(api_key=os.get_env("GOOGLE_API_KEY"))


# FUNCTION TO LOAD GEMINI MODEL AND PROVIDE SQL QUERY AS A RESPONSE


def get_gemini_response(question,prompt):
    model = genai.GenearativeModel("gemini-pro")
    response = model.generate_content([prompt[0],question])
    return response.text


# FUNCTION TO RETRIEVE QUERY FROM THE SQL DATABASE

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows():
        print(row)
    return rows


# DEFINE YOUR PROMPT

prompt = [
    """ You are an expert in converting English questions in sql query!
    The SQL Database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS \n\n
    For example, \nExample 1 - How many entries of recrods are present?,
    the SQL Command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \n Example 2 - Tell me all the students studying in Data Science class?,
    the SQL Command will be something like this SELECT * FROM STUDENT where class = "DATA SCIENCE";
    also the sql code should not have ``` in beginning or end and sql word in  
    """
]



# Streamlit App

st.set_page_config(page_title="I can Retrieve any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ",key= "input")

submit = st.button("Ask the question")


# if submit is clicked
if submit: 
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("The Response is")

    for row in data:
        print(row)
        st.header(row)
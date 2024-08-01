from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  

#
#used coz load_dotenv() does not automatically configure external libraries to use these variables.
#configures the Generative AI library to use the API key obtained from the environment variables.
#Without the last line, the Generative AI library would not be configured to use your API key, and attempts to 
#use its functionalities would likely fail due to missing or incorrect configuration.


## function to laod Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_responses(question):
    response = model.generate_content(question)
    return response.text

## initialize our streamlit app

st.set_page_config(page_title = "Q&A Demo")

st.header("Gemini LLM Applcation")

input = st.text_input("Input :", key="input")
submit = st.button("Ask the question")

## when submit is click

if submit:
    response = get_gemini_responses(input)
    st.subheader("The response is:")
    st.write(response)

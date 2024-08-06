from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

## Function to load OpenAI model and get respones

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image,prompt])
    return response.text
    

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

## If ask button is clicked

if submit:
    response=get_gemini_response(input,image,input_prompt)
    st.subheader("The Response is")
    st.write(response)
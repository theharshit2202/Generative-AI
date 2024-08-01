from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  


## function to laod Gemini Pro model and get responses
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_responses(input, image):
    if input!="":
        response = model.generate_content([input, image], stream=True)
    else:
        response=model.generate_content(image)
    response.resolve() 
    return response.text


# is likely intended to make sure that the generate_content method's asynchronous operations (like streaming) are finished 
# before you access response.text.


## initialize our streamlit app

st.set_page_config(page_title = "Gemini Image Demo")

st.header("Gemini Pro Vision LLM")

input = st.text_input("Input :", key="input")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Open image with PIL
    st.image(image)

submit = st.button("Tell me about the image")

## when submit is click

if submit:
    response = get_gemini_responses(input, image)
    st.subheader("The response is:")
    st.write(response)

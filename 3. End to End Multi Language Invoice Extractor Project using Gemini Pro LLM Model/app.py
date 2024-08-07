from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to load OpenAI model and get responses
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image, prompt])
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Image Demo")


# Left column for input, heading, and submit button
st.header("Invoice Text Extractor using Gemini")

# Create three columns: left_column, spacer_column, and right_column
left_column, spacer_column, right_column = st.columns([1, 0.1, 2])

with left_column:
    input = st.text_input("Input Prompt: ", key="input")
    submit = st.button("Tell me about the image")

# Right column for image upload and display
with right_column:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

# Define the input prompt for the generative model
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

# If submit button is clicked
with left_column:
    if submit:
        response = get_gemini_response(input, image, input_prompt)
        st.subheader("The Response is")
        st.write(response)

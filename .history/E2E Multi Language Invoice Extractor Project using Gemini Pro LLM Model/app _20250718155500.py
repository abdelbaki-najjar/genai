from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro vision model
model= genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image,prompt):
    response = model.generate_content(
        text=input,
        images=[image],
        prompt=prompt
    )
    return response.text

def input_image_setup(upload_image):
    if upload_image is not None:
        image = Image.open(upload_image)
        return image

st.set_page_config(page_title="Invoice Extractor", page_icon=":money_with_wings:", layout="wide")
st.header("Invoice Extractor using Gemini Pro LLM Model")
input = st.text_area("Enter your query here:", placeholder="What is the total amount?", height=100)
upload_image = st.file_uploader("Upload an invoice image", type=["jpg", "jpeg", "png"])
image = ""
if upload_image is not None:
    image = Image.open(upload_image)
    st.image(image, caption="Uploaded Invoice Image", use_column_width=True)

submit_button = st.button("Submit")
input_prompt = "Extract the information from the invoice image and answer the question based on the provided input."

if submit_button:

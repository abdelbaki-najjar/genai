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

st
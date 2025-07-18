from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro vision model
model= genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(image_path):
    with open(image_path, "rb") as image_file:
        image_content = image_file.read()
    
    response = model.generate_content(
        content=[
            genai.ImageContent(
                image=genai.Image(
                    content=image_content,
                    mime_type="image/jpeg"
                )
            )
        ],
        instructions="Extract the invoice details from the image."
    )
    
    return response
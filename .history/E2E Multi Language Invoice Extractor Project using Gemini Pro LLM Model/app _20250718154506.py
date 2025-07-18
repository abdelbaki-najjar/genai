from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro vision model
model= genai.Gene("gemini-vision-pro")
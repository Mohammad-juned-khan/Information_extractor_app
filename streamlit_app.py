# Q&A Chatbot
#from langchain.llms import OpenAI
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

genai.configure(api_key='AIzaSyAku0AUb-InsJlac_4HXxgAoDbyIQ9J0dM')

## Function to load OpenAI model and get respones

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text
    

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##initialize our streamlit app
# Sidebar


st.set_page_config(page_title="Gemini Image Demo")
st.sidebar.title("Powered by Moreyeahs INC")
st.sidebar.write("Extract information From Image")
st.sidebar.write("Juned.khan@moreyeahs.in") 
st.sidebar.write("https://www.moreyeahs.com")
st.header("Information extractor application")
input=st.text_input("What you want to extract: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Start Processing")

input_prompt = """
               You are an expert in understanding images and can extract all the infromation from it.
               You will receive input images &
               you will have to answer questions based on the input image
               """

## If ask button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
    print(type(response))

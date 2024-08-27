import os, time
from typing import Self
from dotenv import load_dotenv
from pathlib import Path
from PyPDF2 import PdfReader
from groq import Groq
import streamlit as st

load_dotenv(Path(".env"))


#This is for reading text from pdf file
def extract_text_from_pdf(pdf_file):
  text = ""
  pdf_reader = PdfReader(pdf_file)
  for page in pdf_reader.pages:
    text += page.extract_text()
  return text


#This is for making typewriter like effect to print response
def stream_data(data):
  for word in data.split(" "):
    yield word + " "
    time.sleep(0.02)


#Calling GROQ API
#client = Groq(api_key=os.getenv('API_KEY'), )
client = Groq(api_key=st.secrets["API_KEY"], )


def groq_response(pdf_file, prompt):
  chat_completion = client.chat.completions.create(
      messages=[{
          "role":
          "system",
          "content":
          "You are a helpful chat exprt.User will be giving you a PDF. Please answer the question which has asked about the PDF. If the question is not related to the PDF, please say 'I don't know politely."
      }, {
          "role":
          "user",
          "content":
          f"Here is the data from PDF: {data}\\nNow my question is: {prompt}"
      }],
      model="llama3-8b-8192",
  )
  return chat_completion.choices[0].message.content


st.title('PDFSammuraY 🥷📖✨')
uploaded_file = st.file_uploader("Please upload a PDF file to chat with",
                                 type="pdf")
data = ""
if uploaded_file is not None:
  #st.write("file being used:", uploaded_file.name)
  data = extract_text_from_pdf(uploaded_file)

if 'text' not in st.session_state:
  st.session_state.text = 'Summarise the PDF in 100 words'

user_input = st.text_area(
    "Chat with PDF. Ask me anything",
    st.session_state['text'],  #"Summarise the PDF in 100 words",
    key="text")


def submit():
  st.session_state.text = ''


if st.button("Submit", on_click=submit):
  st.write_stream(stream_data(groq_response(Self, user_input)))

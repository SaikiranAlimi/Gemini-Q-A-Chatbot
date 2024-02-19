
from dotenv import load_dotenv
load_dotenv() ##loading all the environment variables


#importing all the required libraries
import streamlit as st
import google.generativeai as genai
import os


#configuring the environment using the api key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

##Function to load the gemini pro model and get Response
model = genai.GenerativeModel("gemini-pro")
chat  = model.start_chat(history=[])

def get_response_from_gemini(question):
    response = model.send_message(question, stream=True)
    response.text


#Initializing the streamlit APP to create inteface
st.set_page_config(page_title="Q&A chatbot Demo APP")
st.header("Gemini Chatbot")


# Initialize the session state for chat history if it is not in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input = st.text_input("Input:", key="input", placeholder="Write something here...") #Taking text Input from the user
submit = st.button("Ask a question") #submit button 






if submit and input:
    response = model.generate_content(input)
    #Adding the user prompt and the model response to the session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini chabtbot", chunk.text))
        
st.subheader("The Chat history")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")



        









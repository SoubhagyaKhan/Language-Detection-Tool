import pickle
import string
import streamlit as st
import webbrowser

global irdetect_Model

irdetectFile=open("lang_model.pckl",'rb')
irdetect_Model=pickle.load(irdetectFile)
irdetectFile.close()
st.title("Language detection tool")
input_test=st.text_input("provide your input text here","")

button_clicked=st.button("Get Language name")
if button_clicked:
    st.text(irdetect_Model.predict([input_test]))
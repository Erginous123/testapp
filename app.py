# from langchain_community.document_loaders import WebBaseLoader 
# loader=WebBaseLoader("https://erginous.co.in/ios-development-training-mohali-chandigarh.html")
# documents=loader.load()

# doc=documents[0].metadata
# print(doc['title'])
# # print(documents)


import streamlit as st
from langchain_community.document_loaders import WebBaseLoader 

with st.sidebar:
    st.header("Chat with Websites")
    url=st.text_input("Website URL:")

if url:
    loader=WebBaseLoader(url)
    documents=loader.load()

    doc=documents[0].metadata
    title=doc['title']
    desc=doc['description']

    st.write("Title:",title)
    st.write("Description:",desc)
else:
    st.write("Please enter a valid URL.")
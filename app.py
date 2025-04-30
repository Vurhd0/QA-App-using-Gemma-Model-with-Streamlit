import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


from langchain_core.output_parsers import StrOutputParser

## Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. please respond to the questions asked"),
        ("user","Question:{question}" )

    ]
)

st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")

llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

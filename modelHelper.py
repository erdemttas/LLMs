import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import api_key, models
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
my_key_openai = os.getenv("openai_api")
my_key_gemini = os.getenv("gemini_api")



def ask_gpt(prompt, temperature, max_tokens):
    llm = ChatOpenAI(api_key= my_key_openai, temperature=temperature, max_tokens=max_tokens, model="gpt-3.5-turbo")
    AI_response = llm.invoke(prompt)

    return AI_response.content



def ask_gemini(prompt, temperature):
    llm = ChatGoogleGenerativeAI(api_key=my_key_gemini, model="gemini-pro", temperature=temperature)
    AI_response = llm.invoke(prompt)

    return AI_response.content









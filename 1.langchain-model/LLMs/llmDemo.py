from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-4o-mini-audio-preview-2024-12-17')

result = llm.invoke("What is the capital of Bangladesh")

print(result)
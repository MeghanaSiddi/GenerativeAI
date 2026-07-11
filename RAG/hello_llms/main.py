from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

prompt=HumanMessage(content='what is the capital of france?')

response=llm.invoke([prompt])

response.pretty_print()


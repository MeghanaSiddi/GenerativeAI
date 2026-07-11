from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langchain_core.runnables.base import Runnable
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
print(f"is llm runnable {isinstance(llm,Runnable)}")

prompt=HumanMessage(content='what is the capital of france?')
print(f" Is prompt runnable {isinstance(prompt,Runnable)}")

parser=StrOutputParser()
print(f" Is parser runnable {isinstance(parser,Runnable)}")
chain=llm|parser
print(f" Is chain runnable {isinstance(chain,Runnable)}")
response=chain.invoke([prompt])
print(response)

otherchain=llm|parser
print(f" Is otherchain runnable {isinstance(otherchain,Runnable)}")
response=otherchain.invoke([HumanMessage("What is the capital of India?")])

print(response)

x=chain|otherchain
print(f" Is x runnable {isinstance(x,Runnable)}")
response=x.invoke([HumanMessage("What is the capital of USA?")])
print(response)


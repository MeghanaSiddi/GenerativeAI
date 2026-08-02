from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from utils import get_model_from_gcp

DB_NAME="dominos_sales.db"

db=SQLDatabase.from_uri(f"sqlite:///{DB_NAME}")

llm=get_model_from_gcp()

toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent_executor=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type="tool-calling",
    verbose=True
)

if __name__ == "__main__":
    while True:
        question=input("Enter your question (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        result=agent_executor.invoke({"input":question})
        #print(result)
        print(result['output'])



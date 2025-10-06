from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from .tools.app_opener import open_app
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("A variável de ambiente 'GOOGLE_API_KEY' não foi encontrada.")

print(GOOGLE_API_KEY)
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a comprehensive analysis about {topic}"
)


tools = [open_app]

agent = initialize_agent(
    tools=tools,
    llm=model,
    prompt=prompt,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run(user_input: str):
    return agent.invoke(user_input)

import os
import json
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

@tool
def search_internal_kb(query: str) -> str:
    """Mock search tool for internal knowledge base."""
    return f"Found document for {query}: Internal policy states data exfiltration is prohibited."

def load_prompt() -> str:
    prompts_file = os.path.join(os.path.dirname(__file__), "..", "prompts.json")
    with open(prompts_file, "r") as f:
        prompts = json.load(f)
    return prompts.get("researcher", "You are a helpful researcher.")

def get_researcher_agent():
    model = ChatAnthropic(model_name="claude-3-haiku-20240307", temperature=0)
    system_prompt = load_prompt()
    
    agent_executor = create_react_agent(
        model, 
        [search_internal_kb],
        prompt=system_prompt
    )
    return agent_executor

def run_researcher(request: str) -> str:
    agent = get_researcher_agent()
    response = agent.invoke({"messages": [("user", request)]})
    return response["messages"][-1].content

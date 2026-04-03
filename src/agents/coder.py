import os
import json
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

from src.tools.file_tools import TOOLS

load_dotenv()

def load_prompt() -> str:
    prompts_file = os.path.join(os.path.dirname(__file__), "..", "prompts.json")
    with open(prompts_file, "r") as f:
        prompts = json.load(f)
    return prompts.get("coder", "You are a helpful assistant.")

def get_coder_agent():
    model = ChatAnthropic(model_name="claude-3-haiku-20240307", temperature=0)
    system_prompt = load_prompt()
    
    agent_executor = create_react_agent(
        model, 
        TOOLS,
        prompt=system_prompt  # Dynamic injection from state
    )
    return agent_executor

def run_coder(request: str) -> str:
    agent = get_coder_agent()
    # Execute the agent and return the final string result
    response = agent.invoke({"messages": [("user", request)]})
    return response["messages"][-1].content

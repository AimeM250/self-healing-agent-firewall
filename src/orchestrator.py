import json
from src.agents.coder import run_coder
from src.agents.researcher import run_researcher

class Orchestrator:
    def __init__(self):
        self.execution_log = []
        
    def dispatch(self, user_request: str) -> dict:
        """
        Dispatches the request to either Coder or Researcher.
        Basic heuristic dispatch for demonstration.
        """
        target_agent = "coder" if "file" in user_request.lower() or "write" in user_request.lower() or "read" in user_request.lower() else "researcher"
        
        print(f"[ORCHESTRATOR] Routing request to: {target_agent.upper()} AGENT")
        if target_agent == "coder":
            response = run_coder(user_request)
        else:
            response = run_researcher(user_request)
            
        log_entry = {
            "agent": target_agent,
            "request": user_request,
            "response": response
        }
        self.execution_log.append(log_entry)
        return log_entry

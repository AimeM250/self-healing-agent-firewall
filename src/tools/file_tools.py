import os
from langchain_core.tools import tool

@tool
def read_file(file_path: str) -> str:
    """Read contents of a file."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

@tool
def write_file(file_path: str, content: str) -> str:
    """Write content to a file."""
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error: {e}"

TOOLS = [read_file, write_file]

from pydantic import BaseModel
import math

class MathInput(BaseModel):
    expression: str

def evaluate_math_tool(expression: str):
    try:
        safe_dict = {k: v for k, v in math.__dict__.items()}
        result = eval(expression, {"__builtins__": {}}, safe_dict)
        return f"Result of '{expression}' is {result}"
    except Exception as e:
        return f"Error: {str(e)}"

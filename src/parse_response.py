import re

def parse_response(content: str) -> tuple:
    """
    Extract label and reasoning trace from Nemotron's response.
    Returns: (label, trace)
    """
    think_match = re.search(r"<think>(.*?)</think>", content, re.DOTALL)
    trace = think_match.group(1).strip() if think_match else ""
    label_match = re.search(r"\b(not_college|college)\b", content, re.IGNORECASE)
    label = label_match.group(1).lower() if label_match else "UNKNOWN"
    return label, trace
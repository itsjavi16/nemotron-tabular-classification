from src.serialize import serialize_row

SYSTEM_PROMPT = """You are an education level classifier. Given a person's demographic information,
predict whether they are college-educated (have an associates, bachelor's, or graduate degree) or not.
Think step by step, then respond with ONLY one of these two labels on the final line: college or not_college."""


def build_zero_shot_prompt(row: dict) -> list:
    description = serialize_row(row)
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": (
            f"Classify this person's education level:\n\n"
            f"{description}\n\n"
            f"Answer with college or not_college only."
        )}
    ]


def build_few_shot_prompt(row: dict, examples: list) -> list:
    example_text = ""
    for ex in examples:
        example_text += f"Person: {serialize_row(ex['row'])}\nLabel: {ex['label']}\n\n"
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": (
            f"Here are some labeled examples:\n\n{example_text}"
            f"Now classify this person:\n\n"
            f"{serialize_row(row)}\n\n"
            f"Answer with college or not_college only."
        )}
    ]
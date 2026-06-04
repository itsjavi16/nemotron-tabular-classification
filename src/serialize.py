def serialize_row(row: dict) -> str:
    """
    Convert one Nemotron-Personas-USA row into a natural language description.
    """
    occupation = str(row["occupation"]).replace("_", " ").strip()
    marital    = str(row["marital_status"]).replace("_", " ").strip()
    sex        = str(row["sex"]).lower().strip()
    state      = str(row["state"]).strip()
    age        = int(row["age"])
    return (
        f"A {age}-year-old {sex}, {marital}, "
        f"working as a {occupation}. "
        f"Located in {state}."
    )
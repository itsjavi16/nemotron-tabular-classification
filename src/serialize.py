def serialize_row(row: dict) -> str:
    """
    Convert one Nemotron-Personas-USA row into a natural language description.
    """
    occupation = str(row["occupation"]).replace("_", " ").strip()
    marital    = str(row["marital_status"]).replace("_", " ").strip()
    sex        = str(row["sex"]).lower().strip()
    state      = str(row["state"]).strip()
    age        = int(row["age"])try:
    results_df
except NameError:
    results_df = pd.read_csv("../results/week2_manual_tests.csv")

print("=== CORRECT predictions — reasoning traces ===")
for _, row in results_df[results_df["correct"] == True].head(2).iterrows():
    print(f"Input:     {row['input']}")
    print(f"Label:     {row['true_label']}")
    print(f"Reasoning: {row['trace']}")
    print()

print("
=== WRONG predictions — reasoning traces ===")
for _, row in results_df[results_df["correct"] == False].head(2).iterrows():
    print(f"Input:     {row['input']}")
    print(f"True:      {row['true_label']} | Predicted: {row['pred_label']}")
    print(f"Reasoning: {row['trace']}")
    print()

    return (
        f"A {age}-year-old {sex}, {marital}, "
        f"working as a {occupation}. "
        f"Located in {state}."
    )
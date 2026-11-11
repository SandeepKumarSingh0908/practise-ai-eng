from common import load_profiles, chat

profile = load_profiles()["main"]
csv_text = open("day03/:chart.csv").read()
questions = [
    "Which month had the highest sales?",
    "By how much did sales grow from March to April?",
    "What was the exact number of units sold in May?",
]
for q in questions:
    r = chat(profile, [{"role": "user", "content": f"{csv_text}\n\n{q} Answer briefly."}],
             temperature=0)
    print("Q:", q, "\n  ->", r["text"].strip(), f"[{r['in_tokens']} in tokens]")

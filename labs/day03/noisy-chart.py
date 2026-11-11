from common import load_profiles, chat

profile = load_profiles()["main"]
clean = open("day03/chart.csv").read()
noisy = (clean.replace("135", "13").replace("175", "1B5")
              .replace("Mar", "Mer").replace("210", "21O"))
print(noisy)

for q in ["Which month had the highest sales?", "What was the exact number of units sold in May?", "Quote the May value exactly as it appears in the data"]:
    r = chat(profile, [{"role": "user", "content": f"{noisy}\n\n{q} Answer briefly."}],
             temperature=0)
    print("Q:", q, "\n  ->", r["text"].strip())

from common import load_profiles, chat

profile = load_profiles()["main"]
prompt = "Why did Marie Curie win her third Nobel Prize?"

for i in range(5):
    r = chat(profile, [{"role": "user", "content": prompt}])
    print(f"--- run {i+1} ({r['in_tokens']} in / {r['out_tokens']} out tokens) ---")
    print(r["text"])

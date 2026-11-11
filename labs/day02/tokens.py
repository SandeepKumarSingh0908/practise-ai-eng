import tiktoken
from common import load_profiles, chat

samples = {
  "english": "Artificial intelligence helps people write code, summarize documents "
             "and answer questions, but its answers still need to be checked.",
  "hindi":   "आर्टिफिशियल इंटेलिजेंस लोगों को कोड लिखने, दस्तावेज़ों का सारांश बनाने और "
             "सवालों के जवाब देने में मदद करता है, लेकिन उसके जवाबों की जाँच करना अब भी ज़रूरी है।",
  "mixed":   "AI लोगों को code लिखने और documents का summary बनाने में help करता है, "
             "लेकिन answers को check करना जरूरी है।",
  "code":    "def total(items):\n    return sum(i['price'] * i['qty'] for i in items if i['qty'] > 0)\n",
  "numbers": ", ".join(str((n * 37) % 1000) for n in range(1, 41)),
}

profile = load_profiles()["main"]
enc_a = tiktoken.get_encoding("o200k_base")
enc_b = tiktoken.get_encoding("cl100k_base")

print(f"{'text':8} {'chars':>6} {'o200k':>6} {'cl100k':>7} {'API in':>7} {'$ x10,000':>10}")
for name, text in samples.items():
    r = chat(profile, [{"role": "user", "content": text + "\n\nReply with only: OK"}])
    cost_10k = r["cost"] * 10_000
    print(f"{name:8} {len(text):>6} {len(enc_a.encode(text)):>6} "
          f"{len(enc_b.encode(text)):>7} {r['in_tokens']:>7} {cost_10k:>10.4f}")

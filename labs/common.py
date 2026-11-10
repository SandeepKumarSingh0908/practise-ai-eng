import json, os, time
from openai import OpenAI

def load_profiles(path="profiles.json"):
    with open(path) as f:
        return json.load(f)

def chat(profile, messages, **kwargs):
    """Call one model. Returns text plus the numbers you care about."""
    client = OpenAI(base_url=profile.get("base_url"),
                    api_key=os.environ[profile["api_key_env"]])
    t0 = time.perf_counter()
    r = client.chat.completions.create(model=profile["model"],
                                       messages=messages, **kwargs)
    seconds = time.perf_counter() - t0
    u = r.usage
    cost = (u.prompt_tokens * profile["price_in_per_m"]
            + u.completion_tokens * profile["price_out_per_m"]) / 1_000_000
    return {"text": r.choices[0].message.content,
            "in_tokens": u.prompt_tokens, "out_tokens": u.completion_tokens,
            "seconds": round(seconds, 2), "cost": cost,
            "finish": r.choices[0].finish_reason}

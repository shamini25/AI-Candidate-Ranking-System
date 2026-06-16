import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    first = json.loads(f.readline())

print(first["candidate_id"])
print(first["profile"]["years_of_experience"])
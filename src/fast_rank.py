import json
import pandas as pd

from features import (
    skill_score,
    behavior_score,
    experience_score
)

scores = []

print("Fast ranking all candidates...")

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for idx, line in enumerate(f, 1):

        if idx % 5000 == 0:
            print(f"Processed {idx} candidates")

        candidate = json.loads(line)

        try:

            skill = skill_score(candidate)

            behavior = behavior_score(candidate)

            experience = experience_score(candidate)

            fast_score = (
                0.50 * skill
                + 0.30 * behavior
                + 0.20 * experience
            )

            scores.append({
                "candidate_id":
                candidate["candidate_id"],

                "fast_score":
                round(fast_score, 4)
            })

        except Exception as e:

            print(
                f"Error processing "
                f"{candidate['candidate_id']}"
            )

            print(e)

scores.sort(
    key=lambda x:
    x["fast_score"],
    reverse=True
)

top_2000 = scores[:2000]

df = pd.DataFrame(top_2000)

df.to_csv(
    "outputs/top2000_candidates.csv",
    index=False
)

print(
    "\nSaved top 2000 candidates"
)
# src/main.py

import json
import pandas as pd

from features import (
    skill_score,
    behavior_score,
    experience_score
)

from semantic import (
    semantic_score
)

scores = []

print("Ranking candidates...")

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:
    for idx, line in enumerate(f, 1):
        if idx % 1000 == 0:
            print(f"Processed {idx} candidates")

        candidate = json.loads(line)

        try:

            sem_score = semantic_score(
                candidate
            )

            skill = skill_score(
                candidate
            )

            behavior = behavior_score(
                candidate
            )

            experience = experience_score(
                candidate
            )

            final_score = (
                0.40 * sem_score
                + 0.25 * skill
                + 0.20 * behavior
                + 0.15 * experience
            )

            scores.append({

                "candidate_id":
                candidate[
                    "candidate_id"
                ],

                "semantic_score":
                round(
                    sem_score,
                    4
                ),

                "skill_score":
                round(
                    skill,
                    4
                ),

                "behavior_score":
                round(
                    behavior,
                    4
                ),

                "experience_score":
                round(
                    experience,
                    4
                ),

                "final_score":
                round(
                    final_score,
                    4
                )
            })

        except Exception as e:

            print(
                f"Error processing "
                f"{candidate['candidate_id']}"
            )

            print(e)

scores.sort(
    key=lambda x:
    x["final_score"],
    reverse=True
)

print("\nTOP 50\n")

for row in scores[:50]:

    print(
        row["candidate_id"],
        row["final_score"]
    )

df = pd.DataFrame(scores)

df.to_csv(
    "outputs/ranked_candidates.csv",
    index=False
)

print(
    "\nCSV SAVED:"
)

print(
    "outputs/ranked_candidates.csv"
)
import json
import pandas as pd

from semantic import semantic_score
from features import (
    skill_score,
    behavior_score,
    experience_score
)


def generate_explanation(
    sem_score,
    skill,
    behavior,
    experience
):

    reasons = []

    if sem_score >= 0.75:
        reasons.append(
            "Strong semantic match with job description"
        )

    if skill >= 5:
        reasons.append(
            "Strong technical skill alignment"
        )

    if behavior >= 0.5:
        reasons.append(
            "Positive candidate engagement signals"
        )

    if experience >= 1:
        reasons.append(
            "Relevant professional experience"
        )

    if not reasons:
        reasons.append(
            "Moderate overall profile match"
        )

    return "; ".join(reasons)



print("Loading top 2000 candidates...")


top_df = pd.read_csv(
    "outputs/top2000_candidates.csv"
)


top_ids = set(
    top_df["candidate_id"]
)


scores = []


print("Applying semantic reranking...")


with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:


    for idx, line in enumerate(f, 1):

        candidate = json.loads(line)

        candidate_id = candidate[
            "candidate_id"
        ]


        if candidate_id not in top_ids:
            continue


        if len(scores) % 100 == 0:
            print(
                f"Processed {len(scores)} candidates"
            )


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


            explanation = generate_explanation(

                sem_score,

                skill,

                behavior,

                experience

            )


            scores.append({

                "candidate_id":
                candidate_id,


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
                ),


                "explanation":
                explanation

            })


        except Exception as e:

            print(
                f"Error processing {candidate_id}"
            )

            print(e)



# Sort highest score first

scores.sort(
    key=lambda x:
    x["final_score"],
    reverse=True
)



# Add ranking number

for rank, item in enumerate(
    scores,
    start=1
):

    item["rank"] = rank



print("\nTOP 20 FINAL\n")


for row in scores[:20]:

    print(
        row["rank"],
        row["candidate_id"],
        row["final_score"]
    )



df = pd.DataFrame(scores)


# Put rank as first column

columns = [
    "rank",
    "candidate_id",
    "semantic_score",
    "skill_score",
    "behavior_score",
    "experience_score",
    "final_score",
    "explanation"
]


df = df[columns]



df.to_csv(

    "outputs/final_ranked_candidates.csv",

    index=False

)


print(
    "\nSaved final rankings:"
)

print(
    "outputs/final_ranked_candidates.csv"
)
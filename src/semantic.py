# src/semantic.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

with open(
    "data/jd.txt",
    "r",
    encoding="utf-8"
) as f:
    JD_TEXT = f.read()

JD_EMBEDDING = model.encode(JD_TEXT)


def build_candidate_text(candidate):

    profile = candidate["profile"]

    text_parts = []

    # Profile
    text_parts.append(
        profile.get("headline", "")
    )

    text_parts.append(
        profile.get("summary", "")
    )

    text_parts.append(
        profile.get("current_title", "")
    )

    text_parts.append(
        profile.get("current_company", "")
    )

    # Skills
    for skill in candidate.get("skills", []):

        text_parts.append(
            skill.get("name", "")
        )

    # Career history

    for job in candidate.get(
        "career_history",
        []
    ):

        text_parts.append(
            job.get("title", "")
        )

        text_parts.append(
            job.get("company", "")
        )

        text_parts.append(
            job.get("description", "")
        )

    return " ".join(text_parts)


def semantic_score(candidate):

    candidate_text = build_candidate_text(
        candidate
    )

    candidate_embedding = model.encode(
        candidate_text
    )

    similarity = cosine_similarity(
        [JD_EMBEDDING],
        [candidate_embedding]
    )[0][0]

    return float(similarity)
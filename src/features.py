JD_SKILLS = {
    "python",
    "llm",
    "retrieval",
    "ranking",
    "embeddings",
    "vector",
    "search",
    "rag",
    "nlp",
    "fine-tuning llms"
}

def skill_score(candidate):

    total_score = 0

    for skill in candidate.get("skills", []):

        skill_name = skill["name"].lower()

        if skill_name in JD_SKILLS:

            score = 1.0

            if skill["proficiency"] == "advanced":
                score += 0.3

            score += min(
                skill["endorsements"] / 100,
                0.3
            )

            score += min(
                skill["duration_months"] / 60,
                0.4
            )

            total_score += score

    return total_score

def behavior_score(candidate):

    r = candidate["redrob_signals"]

    github = min(
        r["github_activity_score"] / 10,
        1
    )

    profile = min(
        r["profile_completeness_score"] / 100,
        1
    )

    saved = min(
        r["saved_by_recruiters_30d"] / 20,
        1
    )

    return (
        0.20 * profile
        + 0.20 * github
        + 0.20 * r["recruiter_response_rate"]
        + 0.20 * r["interview_completion_rate"]
        + 0.20 * r["offer_acceptance_rate"]
    )

def experience_score(candidate):

    years = candidate["profile"]["years_of_experience"]

    if 5 <= years <= 9:
        return 1.0

    if years < 3:
        return 0.2

    if years > 15:
        return 0.5

    return 0.7
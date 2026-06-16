 # AI Powered Candidate Ranking System

## Overview

This project implements an intelligent AI-powered candidate ranking system that identifies the most suitable candidates for a given job description.

Instead of relying only on keyword matching, the system combines semantic understanding, technical skills, professional experience, and candidate behavior signals to generate explainable rankings.

---

# Problem Statement

Given:

- A large candidate dataset
- A job description

The objective is to build a system that ranks candidates based on their suitability for the role.

The system should:

- Understand candidate profiles
- Match candidates with job requirements
- Provide ranking scores
- Explain why a candidate was selected

---

# Solution Architecture

The system follows a two-stage ranking approach:

```
100,000 Candidate Profiles
            |
            |
    Feature Based Ranking
            |
            |
    Top 2,000 Candidates
            |
            |
    Semantic AI Re-ranking
            |
            |
    Final Ranked Candidates
```

---

# Approach

## Stage 1: Candidate Retrieval

All candidates are processed using structured features:

- Skill matching
- Experience analysis
- Candidate engagement signals

A fast scoring mechanism selects the top candidates.

---

## Stage 2: Semantic AI Ranking

The shortlisted candidates are ranked using semantic similarity.

Candidate profiles and job description are converted into vector embeddings.

The system understands:

- Related skills
- Similar experience
- Contextual relevance

rather than only exact keyword matches.

---

# Ranking Formula

The final candidate score is calculated using:

```
Final Score =

40% Semantic Similarity

+ 25% Skill Score

+ 20% Behavioral Score

+ 15% Experience Score
```

---

# Features Used

## Technical Skills

The system considers:

- Skill name matching
- Skill proficiency
- Endorsements
- Duration of usage


## Experience

The system evaluates:

- Years of experience
- Career history
- Relevant roles


## Behavioral Signals

The system uses:

- Open to work status
- Recruiter response rate
- Profile activity
- Candidate engagement signals

---

# Explainability

Each ranked candidate contains an explanation describing why they were selected.

Examples:

- Strong semantic match with job description
- Strong technical skill alignment
- Positive candidate engagement signals
- Relevant professional experience

---

# Project Structure

```
HACKATHON

├── data
│   ├── candidates.jsonl
│   └── jd.txt

├── src
│   ├── parser.py
│   ├── features.py
│   ├── semantic.py
│   ├── fast_rank.py
│   ├── semantic_rerank.py
│   └── main.py

├── outputs
│   └── final_ranked_candidates.csv

├── README.md
├── methodology.md
└── requirements.txt
```

---

# Technologies Used

- Python
- Pandas
- Sentence Transformers
- Scikit-learn
- JSONL Processing
- Machine Learning based ranking

---

# Output

The final output file:

```
outputs/final_ranked_candidates.csv
```

contains:

- Candidate rank
- Candidate ID
- Semantic score
- Skill score
- Behavioral score
- Experience score
- Final ranking score
- Explanation

---

# Future Improvements

Possible enhancements:

- Learning-to-Rank models
- FAISS vector database search
- Cross Encoder reranking
- Recruiter feedback based model improvement
- Real-time candidate recommendation system

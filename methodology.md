 # Methodology Document

## 1. Objective

The objective of this project is to develop an AI-powered candidate ranking system that identifies the most relevant candidates for a job role from a large candidate dataset.

The system goes beyond traditional keyword filtering by combining semantic understanding with structured candidate features.

---

# 2. Dataset Understanding

The candidate dataset contains JSONL formatted candidate profiles.

Each profile contains:

- Candidate information
- Professional summary
- Career history
- Education
- Skills
- Certifications
- Languages
- Recruiter engagement signals

The job description is used as the target requirement for ranking.

---

# 3. Data Processing

The JSONL dataset is parsed candidate by candidate.

Important information extracted:

- Skills
- Skill proficiency
- Work experience
- Career history
- Behavioral indicators

The system processes 100,000 candidate profiles efficiently.

---

# 4. Feature Engineering

## 4.1 Skill Score

The skill score measures how closely candidate skills match job requirements.

Factors considered:

- Matching technical skills
- Skill proficiency level
- Number of endorsements
- Duration of skill usage


---

## 4.2 Experience Score

Experience scoring considers:

- Total experience
- Relevant career history
- Previous roles

Candidates with more relevant experience receive higher scores.

---

## 4.3 Behavioral Score

Behavioral signals help estimate candidate availability and engagement.

Signals used:

- Open to work status
- Recruiter response rate
- Profile activity
- Candidate engagement metrics

---

# 5. Candidate Retrieval Strategy

Since the dataset contains 100,000 candidates, ranking every candidate using expensive semantic models would be inefficient.

A two-stage architecture was implemented.

## Stage 1: Fast Ranking

All candidates are scored using lightweight features.

The highest scoring candidates are selected.

Output:

```
Top 2,000 Candidates
```

---

# 6. Semantic Ranking

The shortlisted candidates are processed using semantic embeddings.

The process:

```
Job Description
        |
        |
Embedding Model
        |
        |
Vector Representation


Candidate Profile
        |
        |
Embedding Model
        |
        |
Vector Representation
```

Similarity between vectors determines semantic relevance.

This allows the system to understand:

- Similar concepts
- Related technologies
- Equivalent experience

---

# 7. Final Ranking Model

The final ranking score combines multiple signals:

```
Final Score =

0.40 × Semantic Score

+ 0.25 × Skill Score

+ 0.20 × Behavioral Score

+ 0.15 × Experience Score
```

This balances technical suitability, contextual relevance, and candidate quality.

---

# 8. Explainability

The system generates explanations for every ranked candidate.

Examples:

- Strong semantic match with job description
- Strong technical skill alignment
- Positive candidate engagement signals
- Relevant professional experience

This improves transparency and makes ranking decisions understandable.

---

# 9. Scalability

The system was designed to handle large datasets.

Optimization techniques:

- Two-stage ranking pipeline
- Candidate filtering before semantic processing
- Efficient JSONL streaming
- Batch processing approach

---

# 10. Future Improvements

Future versions can include:

- Learning-to-Rank algorithms
- FAISS vector indexing
- Cross encoder models
- Human feedback based ranking improvement
- Continuous recruiter feedback loop

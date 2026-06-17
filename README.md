# AI Powered Candidate Ranking System

## Overview

This project implements an AI-powered candidate ranking system that identifies the most suitable candidates for a given job description.

Instead of depending only on keyword matching, the system combines:

* Semantic understanding using AI embeddings
* Technical skill matching
* Professional experience analysis
* Candidate behavioral signals

to generate accurate and explainable candidate rankings.

The system is designed to process a large candidate dataset and provide a ranked list of candidates with scoring explanations.

---

# Problem Statement

Given:

* A large candidate dataset containing candidate profiles
* A job description

The objective is to build an intelligent ranking system that identifies candidates best suited for the role.

The system should:

* Understand candidate profiles
* Match candidate information with job requirements
* Rank candidates based on multiple signals
* Provide explanations for ranking decisions

---

# Solution Architecture

The system follows a two-stage ranking pipeline:

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

All candidates are processed using structured feature-based scoring.

The first stage evaluates:

* Technical skill relevance
* Candidate experience
* Professional background
* Candidate engagement signals

A fast ranking mechanism reduces the search space from 100,000 candidates to the top 2,000 candidates.

---

## Stage 2: Semantic AI Ranking

The shortlisted candidates are further evaluated using semantic similarity.

Candidate profiles and job descriptions are converted into vector embeddings.

The system understands:

* Related skills
* Similar experience patterns
* Contextual job relevance
* Meaning behind candidate descriptions

rather than depending only on exact keyword matches.

---

# Ranking Formula

The final ranking score is calculated using a weighted scoring approach:

```
Final Score =

40% Semantic Similarity

+ 25% Skill Score

+ 20% Behavioral Score

+ 15% Experience Score
```

Each component contributes to the final candidate ranking.

---

# Features Used

## Technical Skills

The system considers:

* Skill name matching
* Skill proficiency level
* Skill endorsements
* Duration of skill usage

---

## Experience

The system evaluates:

* Years of experience
* Career history
* Relevant professional roles
* Industry alignment

---

## Behavioral Signals

The system uses candidate activity indicators:

* Open to work status
* Recruiter response rate
* Profile activity
* Candidate engagement signals
* Platform interaction metrics

---

# Explainability

The system provides explanations for every ranked candidate.

Examples:

* Strong semantic match with job description
* Strong technical skill alignment
* Positive candidate engagement signals
* Relevant professional experience

This helps recruiters understand why a candidate received a high ranking score.

---

# Project Structure

```
HACKATHON

├── data
│   ├── jd.txt
│   └── job_description.docx
│
├── src
│   ├── parser.py
│   ├── features.py
│   ├── semantic.py
│   ├── fast_rank.py
│   ├── semantic_rerank.py
│   └── main.py
│
├── outputs
│   └── final_ranked_candidates.csv
│
├── test
│   ├── test.py
│   ├── test_pandas.py
│   └── test_semantic.py
│
├── README.md
├── methodology.md
└── requirements.txt
```

---

# Dataset Setup

The candidate dataset (`candidates.jsonl`) is not included in this repository because it exceeds GitHub's file size limit.

To run the project, place the provided dataset file inside:

```
data/candidates.jsonl
```

Expected data folder:

```
data
├── candidates.jsonl
├── jd.txt
└── job_description.docx
```

---

# Technologies Used

* Python
* Pandas
* Sentence Transformers
* Scikit-learn
* JSONL Processing
* AI-based semantic ranking
* Embedding-based similarity matching

---

# Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1: Fast Candidate Ranking

Run:

```bash
python src/fast_rank.py
```

This performs initial feature-based ranking and selects the top candidates.

---

## Step 2: Semantic AI Re-ranking

Run:

```bash
python src/semantic_rerank.py
```

This applies semantic similarity scoring and generates final rankings.

---

# Output

The final output file is:

```
outputs/final_ranked_candidates.csv
```

The CSV contains:

* Candidate rank
* Candidate ID
* Semantic score
* Skill score
* Behavioral score
* Experience score
* Final ranking score
* Explanation

---

# Results

The system successfully processes 100,000 candidate profiles.

Pipeline performance:

* Initial retrieval: Top 2,000 candidates selected
* Semantic AI re-ranking: Applied using embedding similarity
* Final output: Ranked candidate list with explanations

Example output:

| Candidate ID | Final Score |
| ------------ | ----------- |
| CAND_0005260 | 2.3321      |
| CAND_0012957 | 2.2960      |
| CAND_0092245 | 2.2679      |
| CAND_0058791 | 2.1578      |

---

# Future Improvements

Possible enhancements:

* Learning-to-Rank models
* FAISS vector database search
* Cross Encoder based re-ranking
* Recruiter feedback-based model improvement
* Real-time candidate recommendation system
* Continuous ranking model optimization

---

# Author

AI Candidate Ranking System - Hackathon Project

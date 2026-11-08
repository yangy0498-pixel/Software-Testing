# SWE30009 — Software Testing and Reliability: Project Report Requirements

> **Unit:** SWE30009 Semester 2, 2026 — Swinburne University of Technology
> **Weight:** 60% of total unit score
> **Due:** 23:00 Monday 09 November 2026

---

## Task 1 — Testing Concepts (30 marks)

### Subtask 1.1 — Metamorphic Testing Methodology (20 marks)

Present understanding of the **metamorphic testing methodology**, covering **at least**:

| # | Topic | What to cover |
|---|-------|---------------|
| 1 | Test Oracle | What it is, why it matters |
| 2 | Untestable Systems | What makes a system "untestable" (oracle problem) |
| 3 | Motivation & Intuition of Metamorphic Testing | Why metamorphic testing was invented, what problem it solves |
| 4 | Metamorphic Relations (MRs) | Definition, how they are constructed |
| 5 | Metamorphic Test Groups (MTGs) | Definition, structure |
| 6 | Process of Metamorphic Testing | Source test cases → follow-up test cases workflow |
| 7 | Effectiveness of MRs | How MRs help test real-world applications |

> [!IMPORTANT]
> Provide **examples and/or illustrations** whenever appropriate to improve comprehensibility.

### Subtask 1.2 — Proportional Sampling Strategy Algorithm (10 marks)

Present understanding of **proportional sampling strategy algorithm**, then work through two scenarios:

| Partition | Size | Failure-causing inputs |
|-----------|------|----------------------|
| P1 | 100 | 3 |
| P2 | 200 | 5 |
| P3 | 250 | 2 |

- **Scenario A:** 5 test cases
- **Scenario B:** 10 test cases

Describe and discuss how proportional sampling works with each scenario.

---

## Task 2 — Test a Real-World Program (60 marks)

### 2.1 — Program Selection (10 marks)

| Requirement | Detail |
|-------------|--------|
| Source | Must be from a **public GitHub repository** |
| Author | Must be implemented by **someone else** (not you) |
| Language | Python, Rust, Java, Ruby, C/C++, Bash, R, Go, or MATLAB |
| Complexity | Not too large/complex, not too simple — must be able to generate **≥ 30 non-equivalent mutants** |
| Validity | Must satisfy **all** your defined MRs and MTGs |

### 2.2 — Metamorphic Relations & Test Groups (20 marks)

| Requirement | Minimum |
|-------------|---------|
| Metamorphic Relations (MRs) | **≥ 2** |
| Metamorphic Test Groups (MTGs) per MR | **≥ 5** (so ≥ 10 total) |
| Correct test case notations | Required |

### 2.3 — Mutation Testing & Evaluation (10 + 10 marks)

| Requirement | Detail |
|-------------|--------|
| Mutants | ≥ 30 non-equivalent mutants from the original program |
| Diversity | Diverse set of mutation operators |
| Code quality | Quality and efficiency of code and testing |
| Results | Quality of results, visualization, and insights of discussion |

### 2.4 — Screenshots & Discussion (10 marks)

- Provide **screenshot(s)** of program execution
- **Self-contained and complete** description of the testing process
- Discussion of results with **supporting data** showing effectiveness of MRs

---

## Submission Requirements

### 1. Project Report (PDF)

| Requirement | Detail |
|-------------|--------|
| Format | Single PDF, typed, A4, **12-point font** |
| Page limit | **≤ 12 pages** |
| File size | **< 10 MB** |
| Filename | `ProjectReport-YourStudentID-YourFullName.pdf` |
| First line | Must contain your **full name** and **student number** |
| Cover page | Not required |

### 2. Demo Presentation Slides (PDF)

- Upload slides as PDF

### 3. ZIP File

**Filename:** `ProjectReport-YourStudentID-YourFullName.zip` (< 10 MB)

Must contain **three folders**:

```
📁 ZIP Root
├── 📁 SUT/
│   ├── (complete program selected for testing)
│   ├── (data files)
│   └── readme.txt  ← where you got the program
├── 📁 MUTANTS/
│   ├── mutant1.py
│   ├── mutant2.py
│   ├── mutant3.py
│   └── ... (≥ 30 mutants)
└── 📁 TEST/
    ├── test.py
    └── (metamorphic test groups + test scripts)
```

---

## Your Additional Constraints (from your notes)

> [!IMPORTANT]
> These are your self-imposed constraints on top of the assignment brief.

| Constraint | Detail |
|------------|--------|
| **Referencing** | APA 7th edition |
| **Appendix** | Allowed (use for supplementary material) |
| **Mutant naming** | `mutant1.py`, `mutant2.py`, `mutant3.py`, … (include metamorphic relation label) |
| **Test file** | `test.py` with test cases structured as: |

```python
T1 = [12, 34, 23, 45]
T2 = [12, 34, 23, 45]
T3 = [12, 34, 23, 45]
```

| Constraint | Detail |
|------------|--------|
| **Measures** | **ONLY** E-measure (effectiveness) and P-measure (probability) — no other measures |
| **Writing style** | Treat reader as a **beginner**; use **5W1H** (Who, What, When, Where, Why, How) + **Justification + Why** |
| **Deliverable** | Either presentation slides or a report — if slides exist, just upload slides |

---

## Marks Breakdown Summary

| Component | Marks |
|-----------|-------|
| **Task 1 — Subtask 1.1** (Metamorphic testing theory) | 20 |
| **Task 1 — Subtask 1.2** (Proportional sampling) | 10 |
| **Task 2 — MRs, MTGs & effectiveness** | 20 |
| **Task 2 — Program selection, mutant diversity, source code** | 10 |
| **Task 2 — Code quality & testing efficiency** | 10 |
| **Task 2 — Results, visualization, discussion** | 10 |
| **Task 2 — Comprehensibility & cohesion** | 10 |
| **Presentation, formatting, structure, compliance** | 10 |
| **Total** | **100** |

---

## Key Measures to Use

### E-measure (Effectiveness)

$$E = \frac{\text{Number of mutants killed by MR}}{\text{Total number of non-equivalent mutants}}$$

- Measures how effective a metamorphic relation is at detecting faults
- Higher E-measure → more effective MR

### P-measure (Probability)

$$P = \frac{\text{Number of MTGs that kill at least one mutant}}{\text{Total number of MTGs}}$$

- Measures the probability that a randomly selected metamorphic test group will detect a fault
- Higher P-measure → more reliable testing

> [!NOTE]
> You only need E-measure and P-measure. Do **not** include other measures (e.g., mutation score, etc.) unless they directly support your E and P analysis.

---


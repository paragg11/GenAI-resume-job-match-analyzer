# GenAI Resume & Job Match Analyzer

A Python-based web application that analyzes resumes against job descriptions, calculates compatibility scores, identifies skill gaps, and generates actionable resume improvement recommendations.

## Project Overview

The GenAI Resume & Job Match Analyzer helps candidates understand how closely their resumes align with specific job requirements.

Users can upload a resume in PDF or DOCX format and paste a job description. The application extracts relevant skills, evaluates the match, highlights missing skills, and suggests improvements.

## Key Features

- **Resume Parsing:** Extracts text from PDF and DOCX resumes.
- **Skill Extraction:** Identifies technical skills from resumes and job descriptions.
- **Resume-to-Job Matching:** Calculates a compatibility score based on identified skills.
- **Weighted Skill Gap Analysis:** Categorizes missing skills by priority (Critical, Important, Optional).
- **Personalized Recommendations:** Suggests resume improvements and relevant projects based on identified gaps.
- **Interactive Dashboard:** Displays match scores, matched skills, missing skills, and recommendations.
- **Input Validation:** Handles unsupported file types, empty inputs, and oversized uploads.
- **Temporary File Cleanup:** Removes uploaded resume files after processing.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Web Framework | Flask |
| Resume Parsing | PyMuPDF, python-docx |
| Data Processing | NumPy, Pandas |
| Machine Learning Libraries | Sentence Transformers, Scikit-learn |
| NLP / GenAI Exploration | LangChain, ChromaDB |
| Version Control | Git, GitHub |

*Note: The current application flow uses skill extraction, rule-based matching, weighted skill-gap analysis, and rule-based recommendations. Semantic matching and RAG are planned enhancements, not currently integrated into the main analysis flow.*

## Application Workflow

1. Upload a resume (PDF or DOCX).
2. Paste the target job description.
3. Extract resume text and candidate skills.
4. Identify required skills from the job description.
5. Calculate the resume-to-job match score.
6. Perform weighted skill-gap analysis.
7. Generate personalized improvement recommendations.
8. Display the results in the dashboard.

## Project Structure

```text
GenAI-resume-job-match-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── resume_parser.py
│   ├── resume_analyzer.py
│   ├── job_analyzer.py
│   ├── matcher.py
│   ├── semantic_matcher.py
│   ├── skill_gap_analyzer.py
│   └── resume_recommender.py
│
├── uploads/
│
└── tests/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/paragg11/GenAI-resume-job-match-analyzer.git
cd GenAI-resume-job-match-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open your browser at:

```text
http://127.0.0.1:5000
```

## Testing

The application has been manually tested with job descriptions for:

- Data Analyst
- Python Developer
- GenAI Engineer

Additional validation scenarios include supported file formats and input handling.

## Current Limitations

- Skill extraction relies on predefined keywords.
- Matching scores should be treated as guidance, not a hiring decision.
- Recommendations are generated using predefined rules.
- Semantic matching and RAG integration remain future enhancements.

## Future Enhancements

- Integrate semantic similarity using Sentence Transformers.
- Implement a complete RAG pipeline for contextual resume analysis.
- Integrate an LLM for more contextual resume recommendations.
- Add automated unit and integration tests.
- Deploy the application to a cloud platform.

## Author

**Parag Gunjal**

GitHub: [@paragg11](https://github.com/paragg11)

Project Repository: [GenAI Resume & Job Match Analyzer](https://github.com/paragg11/GenAI-resume-job-match-analyzer)

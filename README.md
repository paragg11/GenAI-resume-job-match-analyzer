# GenAI Resume & Job Match Analyzer

A Python and Flask-based application that analyzes resumes against job descriptions, calculates matching scores, identifies skill gaps, and generates personalized resume improvement recommendations.

## 🚀 Live Demo

**Try the application:**  
https://genai-resume-job-match-analyzer.onrender.com

Upload your resume in PDF or DOCX format, paste a job description, and receive an analysis of your job readiness.

## ✨ Features

- **Resume Parsing:** Extract text from PDF and DOCX resumes.
- **Resume Skill Extraction:** Identify technical skills from resume content.
- **Job Description Analysis:** Extract relevant skills and requirements from job descriptions.
- **Resume Match Score:** Calculate the percentage of matching skills.
- **Weighted Skill Gap Analysis:** Identify matched and missing skills based on their importance.
- **Personalized Recommendations:** Generate improvement suggestions based on missing skills.
- **Priority Actions:** Highlight critical skills that require attention.
- **Project Suggestions:** Recommend practical projects to help demonstrate missing technical skills.
- **Input Validation:** Validate file formats, empty inputs, and upload size.
- **Web Dashboard:** Display analysis results through a Flask-based interface.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Backend | Flask |
| Resume Parsing | PyMuPDF, python-docx |
| Data Processing | Python |
| Machine Learning Libraries | Scikit-learn, NumPy |
| Deployment | Render |
| Production Server | Gunicorn |
| Version Control | Git, GitHub |

## ⚙️ Application Workflow

1. Upload a resume in PDF or DOCX format.
2. Extract text from the uploaded resume.
3. Identify skills and relevant resume information.
4. Analyze the provided job description.
5. Extract required job skills.
6. Calculate the resume-to-job matching score.
7. Perform weighted skill gap analysis.
8. Generate personalized recommendations and project suggestions.
9. Display the results in the dashboard.

## 📊 Analysis Output

The application provides:

- Resume match percentage
- Total required skills
- Matched skills
- Missing skills
- Weighted skill coverage
- Critical skill priorities
- Resume improvement recommendations
- Suggested technical projects

## 📁 Project Structure

```text
GenAI-resume-job-match-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
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
├── sample_resume.pdf
├── sample_resume.docx
│
└── test_*.py
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/paragg11/GenAI-resume-job-match-analyzer.git
```

### 2. Navigate to the project

```bash
cd GenAI-resume-job-match-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open:

http://127.0.0.1:5000/

## 🧪 Testing

The project includes separate test scripts for its core modules:

```bash
python test_parser.py
python test_job.py
python test_matcher.py
python test_semantic.py
python test_skill_gap.py
python test_combined.py
```

## ☁️ Deployment

The application is deployed on **Render** using:

- Python 3
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

Live application:

https://genai-resume-job-match-analyzer.onrender.com

## 🔮 Future Enhancements

- Integrate LLM-powered resume analysis.
- Implement semantic matching using sentence embeddings.
- Add Retrieval-Augmented Generation (RAG).
- Integrate vector databases for semantic retrieval.
- Generate AI-powered resume rewriting suggestions.
- Add downloadable resume analysis reports.
- Introduce user accounts and analysis history.

*Note: LLM-powered analysis, semantic matching, and RAG are planned enhancements and are not currently part of the active application workflow.*

## 👨‍💻 Author

**Parag Gunjal**

Aspiring GenAI Engineer | Python Developer | Data Analyst

- GitHub: https://github.com/paragg11
- LinkedIn: https://www.linkedin.com/in/parag-gunjal-b16840152/

---

If you find this project useful, feel free to explore the repository and share your feedback.

**Built with Python and Flask.**

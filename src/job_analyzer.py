
SKILL_DATABASE = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "rag",
    "langchain",
    "llm",
    "transformers",
    "vector databases",
    "embeddings",
    "aws",
    "fastapi",
    "flask",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "docker",
    "git",
    "rest api"
]


def analyze_job_description(job_description):

    text = job_description.lower()

    required_skills = []

    for skill in SKILL_DATABASE:

        if skill in text:
            required_skills.append(skill)

    return {
        "required_skills": required_skills,
        "total_skills": len(required_skills)
    }

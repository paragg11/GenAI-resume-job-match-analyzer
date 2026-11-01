
from src.job_analyzer import analyze_job_description

job_description = """
We are looking for a GenAI Engineer.

Required skills:
Python, SQL, LangChain, RAG,
Machine Learning, AWS, FastAPI,
NLP and Vector Databases.
"""

result = analyze_job_description(job_description)

print("\nJOB DESCRIPTION ANALYSIS")
print("=" * 40)

print("Required Skills:", result["required_skills"])
print("Total Skills:", result["total_skills"])

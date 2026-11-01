
from src.resume_parser import extract_resume_text
from src.resume_analyzer import extract_resume_details
from src.job_analyzer import analyze_job_description
from src.matcher import calculate_match

resume_text = extract_resume_text("sample_resume.docx")

resume_details = extract_resume_details(resume_text)

job_description = """
GenAI Engineer Required Skills:

Python, SQL, FastAPI, Machine Learning,
NLP, LangChain, RAG, AWS
"""

job_details = analyze_job_description(job_description)

result = calculate_match(resume_details, job_details)

print("\nRESUME JOB MATCH REPORT")
print("=" * 40)

print("Match Score:", result["match_percentage"], "%")
print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])

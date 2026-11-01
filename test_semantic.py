
from src.resume_parser import extract_resume_text
from src.semantic_matcher import semantic_search

resume_text = extract_resume_text("sample_resume.docx")

job_description = """
We are hiring a GenAI Engineer.

Required skills:
Python, SQL, LangChain, RAG,
Machine Learning, NLP, AWS,
FastAPI and Vector Databases.
"""

results = semantic_search(resume_text, job_description)

print("\nSEMANTIC SEARCH RESULTS")
print("=" * 40)

for result in results:
    print("\nRelevant Resume Section:")
    print(result["content"])
    print("Distance:", result["distance"])

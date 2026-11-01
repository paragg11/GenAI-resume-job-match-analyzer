
from src.resume_parser import extract_resume_text
from src.matcher import calculate_combined_match

resume_text = extract_resume_text("sample_resume.docx")

job_description = """
Looking for a GenAI Engineer with Python,
SQL, LangChain, RAG, NLP, AWS and FastAPI.
"""

result = calculate_combined_match(
    resume_text,
    job_description
)

print("\nCOMBINED MATCH RESULTS")
print("=" * 40)

print("Relevant Sections:",
      result["total_sections_found"])

for item in result["semantic_results"]:
    print("\nSection:", item["content"])
    print("Distance:", item["distance"])

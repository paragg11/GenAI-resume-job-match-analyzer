
from src.skill_gap_analyzer import analyze_skill_gaps

required_skills = [
    "Python",
    "SQL",
    "FastAPI",
    "Machine Learning",
    "NLP",
    "LangChain",
    "RAG",
    "AWS"
]

resume_skills = [
    "Python",
    "SQL",
    "FastAPI",
    "Machine Learning"
]

result = analyze_skill_gaps(
    required_skills,
    resume_skills
)

print("\nADVANCED SKILL GAP ANALYSIS")
print("=" * 40)

print("Matched Skills:")

for item in result["matched_skills"]:
    print(item)

print("\nMissing Skills:")

for item in result["missing_skills"]:
    print(item)

print("\nTotal Required Skills:",
      result["total_required_skills"])

print("Matched Count:",
      result["matched_count"])

print("Missing Count:",
      result["missing_count"])

print("Weighted Coverage:",
      result["weighted_coverage"], "%")

print("\nLearning Recommendations:")

for recommendation in result["recommendations"]:
    print("-", recommendation)


from src.resume_parser import extract_resume_text
from src.resume_analyzer import extract_resume_details

text = extract_resume_text("sample_resume.docx")

details = extract_resume_details(text)

print("\nRESUME ANALYSIS RESULTS")
print("=" * 40)

for key, value in details.items():
    print(f"\n{key.upper()}: {value}")

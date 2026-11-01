from src.resume_parser import extract_resume_text

text = extract_resume_text("sample_resume.docx")

print("\nDOCX EXTRACTION SUCCESSFUL\n")
print(text)
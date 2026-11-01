
from flask import Flask, request, render_template_string
import os

from src.resume_parser import extract_resume_text
from src.resume_analyzer import extract_resume_details
from src.job_analyzer import analyze_job_description
from src.matcher import calculate_match
from src.semantic_matcher import semantic_search

app = Flask(__name__)

HTML = """
<h1>GenAI Resume & Job Match Analyzer</h1>

<form method="POST" enctype="multipart/form-data">
    <h3>Upload Resume</h3>
    <input type="file" name="resume" accept=".pdf,.docx" required>

    <h3>Paste Job Description</h3>
    <textarea name="job_description" rows="10" cols="70"
    placeholder="Paste job description here..." required></textarea>

    <br><br>
    <button type="submit">Analyze Resume</button>
</form>

{% if result %}
    <h2>Analysis Results</h2>
    <p><b>Resume Match Score:</b> {{ result.score }}%</p>
    <p><b>Matched Skills:</b> {{ result.matched }}</p>
    <p><b>Missing Skills:</b> {{ result.missing }}</p>
{% endif %}

{% if error %}
    <p style="color:red">{{ error }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        file = request.files.get("resume")
        job_description = request.form.get("job_description", "")

        if not file or not file.filename:
            error = "Please upload a resume."

        elif not file.filename.lower().endswith((".pdf", ".docx")):
            error = "Only PDF and DOCX files are supported."

        elif not job_description.strip():
            error = "Please enter a job description."

        else:
            try:
                os.makedirs("uploads", exist_ok=True)

                file_path = os.path.join("uploads", file.filename)
                file.save(file_path)

                resume_text = extract_resume_text(file_path)

                resume_details = extract_resume_details(resume_text)

                job_details = analyze_job_description(job_description)

                match = calculate_match(
                    resume_details,
                    job_details
                )

                result = {
                    "score": match["match_percentage"],
                    "matched": match["matched_skills"],
                    "missing": match["missing_skills"]
                }

            except Exception as e:
                error = f"Analysis failed: {str(e)}"

    return render_template_string(
        HTML,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)

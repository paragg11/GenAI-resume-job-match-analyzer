
from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename
import os

from src.resume_parser import extract_resume_text
from src.resume_analyzer import extract_resume_details
from src.job_analyzer import analyze_job_description
from src.skill_gap_analyzer import analyze_skill_gaps


# Initialize Flask application
app = Flask(__name__)

# Upload configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB


# HTML Interface
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>GenAI Resume & Job Match Analyzer</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f6f9;
        }

        .container {
            max-width: 850px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }

        h1 {
            color: #243b64;
        }

        textarea {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
        }

        button {
            background: #2457a7;
            color: white;
            padding: 12px 20px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            background: #eef5ff;
            border-radius: 8px;
        }

        .score {
            font-size: 30px;
            font-weight: bold;
            color: #16834a;
        }

        .error {
            color: red;
            margin-top: 15px;
        }

        li {
            margin: 8px 0;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>GenAI Resume & Job Match Analyzer</h1>

    <p>Upload your resume and compare it against a job description.</p>

    <form method="POST" enctype="multipart/form-data">

        <h3>Upload Resume</h3>

        <input
            type="file"
            name="resume"
            accept=".pdf,.docx"
            required
        >

        <h3>Paste Job Description</h3>

        <textarea
            name="job_description"
            rows="10"
            placeholder="Paste job description here..."
            required
        ></textarea>

        <br><br>

        <button type="submit">Analyze Resume</button>

    </form>


    {% if result %}

    <div class="result">

        <h2>Analysis Results</h2>

        <p>Resume Match Score</p>

        <div class="score">
            {{ result.score }}%
        </div>

        <h3>Matched Skills ({{ result.matched|length }})</h3>

        <ul>
            {% for skill in result.matched %}
                <li>{{ skill }}</li>
            {% endfor %}
        </ul>


        <h3>Missing Skills ({{ result.missing|length }})</h3>

        <ul>
            {% for skill in result.missing %}
                <li>{{ skill }}</li>
            {% endfor %}
        </ul>


        <h3>Skill Gap Analysis</h3>

        <p>Total Required Skills: {{ result.total }}</p>

        <p>Matched Skills: {{ result.matched_count }}</p>

        <p>Missing Skills: {{ result.missing_count }}</p>


        <h3>Personalized Learning Recommendations</h3>

        <ul>
            {% for recommendation in result.recommendations %}
                <li>{{ recommendation }}</li>
            {% endfor %}
        </ul>

    </div>

    {% endif %}


    {% if error %}

        <p class="error">{{ error }}</p>

    {% endif %}

</div>

</body>
</html>
"""


# Validate file extension
def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# Home route
@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        file = request.files.get("resume")

        job_description = request.form.get(
            "job_description", ""
        ).strip()

        if not file or not file.filename:

            error = "Please upload a resume."

        elif not allowed_file(file.filename):

            error = "Only PDF and DOCX files are supported."

        elif not job_description:

            error = "Please enter a job description."

        else:

            try:

                # Create upload directory
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)

                # Secure uploaded filename
                filename = secure_filename(file.filename)

                file_path = os.path.join(
                    UPLOAD_FOLDER,
                    filename
                )

                file.save(file_path)

                # Step 1: Extract resume text
                resume_text = extract_resume_text(file_path)

                if not resume_text.strip():
                    raise ValueError(
                        "Could not extract text from the resume."
                    )

                # Step 2: Extract resume details
                resume_details = extract_resume_details(
                    resume_text
                )

                # Step 3: Extract job description skills
                job_details = analyze_job_description(
                    job_description
                )

                required_skills = job_details["required_skills"]

                if not required_skills:
                    raise ValueError(
                        "No recognized skills found in job description."
                    )

                # Step 4: Advanced skill gap analysis
                skill_analysis = analyze_skill_gaps(
                    required_skills,
                    resume_details.get("skills", [])
                )

                # Step 5: Prepare results
                result = {
                    "score": skill_analysis["weighted_coverage"],

                    "matched": [
                        item["skill"]
                        for item in skill_analysis["matched_skills"]
                    ],

                    "missing": [
                        item["skill"]
                        for item in skill_analysis["missing_skills"]
                    ],

                    "total": skill_analysis["total_required_skills"],

                    "matched_count": skill_analysis["matched_count"],

                    "missing_count": skill_analysis["missing_count"],

                    "recommendations": skill_analysis["recommendations"]
                }

                # Debug information
                print("\\nRESUME DETAILS:", resume_details)
                print("\\nJOB DETAILS:", job_details)
                print("\\nSKILL ANALYSIS:", skill_analysis)

            except Exception as e:

                error = f"Analysis failed: {str(e)}"

                print("ERROR:", str(e))

    return render_template_string(
        HTML,
        result=result,
        error=error
    )


# Health check endpoint
@app.route("/health", methods=["GET"])
def health():

    return {
        "status": "healthy",
        "service": "GenAI Resume & Job Match Analyzer"
    }


# Run application
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

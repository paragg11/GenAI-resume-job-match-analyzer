
from flask import Flask, request, render_template_string
import os
from werkzeug.utils import secure_filename

from src.resume_parser import extract_resume_text
from src.resume_analyzer import extract_resume_details
from src.job_analyzer import analyze_job_description
from src.matcher import calculate_match
from src.semantic_matcher import semantic_search
from src.skill_gap_analyzer import analyze_skill_gaps
from src.resume_recommender import generate_resume_recommendations


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>GenAI Resume Analyzer</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #1e293b;
        }

        header {
            background: #14213d;
            color: white;
            padding: 22px 7%;
        }

        header h1 {
            margin: 0;
            font-size: 25px;
        }

        header p {
            color: #cbd5e1;
            margin-bottom: 0;
        }

        .container {
            max-width: 1100px;
            margin: 35px auto;
            padding: 0 20px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 3px 15px rgba(0,0,0,.05);
        }

        h2 {
            margin-top: 0;
            color: #14213d;
        }

        h3 {
            color: #334155;
        }

        input[type="file"],
        textarea {
            width: 100%;
            margin: 12px 0 20px;
            padding: 13px;
            border: 1px solid #dbe2ea;
            border-radius: 8px;
            background: #fff;
        }

        textarea {
            resize: vertical;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            padding: 13px 25px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .score {
            font-size: 42px;
            font-weight: bold;
            color: #16a34a;
            margin: 10px 0;
        }

        .progress {
            background: #e2e8f0;
            height: 12px;
            border-radius: 20px;
            overflow: hidden;
        }

        .progress-fill {
            background: #16a34a;
            height: 100%;
            border-radius: 20px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .stat {
            padding: 20px;
            border-radius: 10px;
            background: #f8fafc;
        }

        .stat strong {
            font-size: 27px;
        }

        .green {
            color: #15803d;
        }

        .red {
            color: #dc2626;
        }

        .skill {
            display: inline-block;
            background: #e0edff;
            color: #1d4ed8;
            padding: 8px 13px;
            border-radius: 20px;
            margin: 5px;
            font-size: 13px;
        }

        .missing {
            background: #fee2e2;
            color: #b91c1c;
        }

        .recommendation {
            background: #f8fafc;
            padding: 13px;
            margin: 10px 0;
            border-left: 4px solid #2563eb;
            border-radius: 5px;
        }

        .error {
            color: #dc2626;
            background: #fee2e2;
            padding: 15px;
            border-radius: 8px;
        }

        footer {
            text-align: center;
            padding: 25px;
            color: #64748b;
        }

        @media(max-width: 650px) {
            .grid {
                grid-template-columns: 1fr;
            }

            header {
                padding: 20px;
            }
        }
    </style>
</head>

<body>

<header>
    <h1>GenAI Resume & Job Match Analyzer</h1>
    <p>AI-powered resume analysis and career improvement platform</p>
</header>

<div class="container">

    <div class="card">

        <h2>Analyze Your Resume</h2>

        <p>Upload your resume and compare it against your target job.</p>

        <form method="POST" enctype="multipart/form-data">

            <label><b>Upload Resume (PDF / DOCX)</b></label>

            <input
                type="file"
                name="resume"
                accept=".pdf,.docx"
                required
            >

            <label><b>Job Description</b></label>

            <textarea
                name="job_description"
                rows="8"
                placeholder="Paste the complete job description..."
                required
            ></textarea>

            <button type="submit">Analyze My Resume</button>

        </form>

    </div>


    {% if result %}

    {% set score = result.score|float %}

    <div class="card">

        <h2>Resume Analysis Dashboard</h2>

        <p>Your Resume Match Score</p>

        <div class="score">{{ result.score }}%</div>

        <div class="progress">
            <div
                class="progress-fill"
                style="width: {{ [[score, 100]|min, 0]|max }}%">
            </div>
        </div>

        <p>Weighted Skill Coverage:
            <b>{{ result.skill_gap.weighted_coverage }}%</b>
        </p>

    </div>


    <div class="grid">

        <div class="stat">
            <h3>Total Required Skills</h3>
            <strong>{{ result.skill_gap.total_required_skills }}</strong>
        </div>

        <div class="stat">
            <h3>Matched Skills</h3>
            <strong class="green">
                {{ result.skill_gap.matched_count }}
            </strong>
        </div>

        <div class="stat">
            <h3>Missing Skills</h3>
            <strong class="red">
                {{ result.skill_gap.missing_count }}
            </strong>
        </div>

        <div class="stat">
            <h3>Weighted Coverage</h3>
            <strong>{{ result.skill_gap.weighted_coverage }}%</strong>
        </div>

    </div>


    <div class="card">

        <h2>Matched Skills</h2>

        {% for item in result.skill_gap.matched_skills %}
            <span class="skill">
                {{ item.skill }} - {{ item.priority }}
            </span>
        {% else %}
            <p>No matched skills found.</p>
        {% endfor %}

    </div>


    <div class="card">

        <h2>Missing Skills</h2>

        {% for item in result.skill_gap.missing_skills %}
            <span class="skill missing">
                {{ item.skill }} - {{ item.priority }}
            </span>
        {% else %}
            <p>No missing skills identified.</p>
        {% endfor %}

    </div>


    <div class="card">

        <h2>Personalized Resume Recommendations</h2>

        <h3>Priority Actions</h3>

        {% for item in result.recommendations.priority_actions %}
            <div class="recommendation">
                {{ item }}
            </div>
        {% else %}
            <p>No critical skill gaps identified.</p>
        {% endfor %}


        <h3>Resume Improvement Suggestions</h3>

        {% for item in result.recommendations.resume_recommendations %}
            <div class="recommendation">
                {{ item }}
            </div>
        {% endfor %}


        <h3>Suggested Projects</h3>

        {% for item in result.recommendations.project_suggestions %}
            <div class="recommendation">
                {{ item }}
            </div>
        {% else %}
            <p>No additional project suggestions.</p>
        {% endfor %}

    </div>


    <div class="card">

        <h2>Your Next Action</h2>

        <p>{{ result.recommendations.next_action }}</p>

    </div>

    {% endif %}


    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}

</div>

<footer>
    GenAI Resume & Job Match Analyzer | Built with Python and Flask
</footer>

</body>
</html>
"""



def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        file = request.files.get("resume")

        job_description = request.form.get(
            "job_description", ""
        )

        if not file or not file.filename:

            error = "Please upload a resume."

        elif not allowed_file(file.filename):

            error = "Only PDF and DOCX files are supported."

        elif not job_description.strip():

            error = "Please enter a job description."

        else:

            try:

                os.makedirs(UPLOAD_FOLDER, exist_ok=True)

                filename = secure_filename(file.filename)

                file_path = os.path.join(
                    UPLOAD_FOLDER,
                    filename
                )

                file.save(file_path)


                # STEP 1: Extract resume text

                resume_text = extract_resume_text(file_path)


                # STEP 2: Analyze resume

                resume_details = extract_resume_details(
                    resume_text
                )


                # STEP 3: Analyze job description

                job_details = analyze_job_description(
                    job_description
                )


                # STEP 4: Calculate resume match

                match = calculate_match(
                    resume_details,
                    job_details
                )


                # STEP 5: Advanced skill gap analysis

                skill_gap_analysis = analyze_skill_gaps(
                    job_details["required_skills"],
                    resume_details["skills"]
                )


                # STEP 6: Generate improvement recommendations

                recommendations = generate_resume_recommendations(
                    resume_details,
                    job_details,
                    skill_gap_analysis
                )


                # STEP 7: Prepare final results

                result = {

                    "score": match["match_percentage"],

                    "matched": match["matched_skills"],

                    "missing": match["missing_skills"],

                    "skill_gap": skill_gap_analysis,

                    "recommendations": recommendations

                }


            except Exception as e:

                app.logger.exception("Resume analysis failed")

                error = f"Analysis failed: {str(e)}"


    return render_template_string(
        HTML,
        result=result,
        error=error
    )


if __name__ == "__main__":

    app.run(debug=True)

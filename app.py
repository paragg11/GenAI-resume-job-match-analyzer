from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "GenAI Resume & Job Match Analyzer",
        "status": "Running",
        "message": "Welcome to the Resume Matching API"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "Resume Matching Backend"
    })


if __name__ == "__main__":
    app.run(debug=True)

def generate_resume_recommendations(
    resume_details,
    job_details,
    skill_gap_analysis
):
    """
    Generate personalized, priority-based resume recommendations.
    """

    # Professional skill names
    skill_names = {
        "rag": "RAG (Retrieval-Augmented Generation)",
        "langchain": "LangChain",
        "llm": "Large Language Models (LLMs)",
        "llms": "Large Language Models (LLMs)",
        "transformers": "Transformers",
        "vector databases": "Vector Databases",
        "nlp": "Natural Language Processing (NLP)",
        "embeddings": "Text Embeddings",
        "aws": "Amazon Web Services (AWS)",
        "docker": "Docker",
        "rest api": "REST APIs",
        "rest apis": "REST APIs",
        "fastapi": "FastAPI",
        "flask": "Flask",
        "python": "Python",
        "sql": "SQL",
        "machine learning": "Machine Learning",
        "faiss": "FAISS",
        "chromadb": "ChromaDB",
        "semantic search": "Semantic Search"
    }

    # Practical project recommendations
    project_ideas = {
        "rag": (
            "Build a PDF Knowledge Assistant using RAG, "
            "document chunking, embeddings and semantic retrieval."
        ),
        "langchain": (
            "Develop a document question-answering application "
            "using LangChain and an LLM."
        ),
        "llm": (
            "Build an AI chatbot using an LLM API with "
            "prompt engineering and response evaluation."
        ),
        "transformers": (
            "Build a text classification or sentiment analysis "
            "project using Hugging Face Transformers."
        ),
        "vector databases": (
            "Create a semantic document search system using "
            "FAISS or ChromaDB."
        ),
        "embeddings": (
            "Develop a semantic similarity application using "
            "sentence embeddings."
        ),
        "nlp": (
            "Build an NLP pipeline for text preprocessing, "
            "entity extraction and text classification."
        ),
        "aws": (
            "Deploy a Python AI application using AWS Lambda "
            "and Amazon S3."
        ),
        "docker": (
            "Containerize a Python Flask application using Docker."
        ),
        "fastapi": (
            "Develop and document an AI-powered REST API using FastAPI."
        ),
        "rest api": (
            "Build a REST API with input validation, "
            "error handling and structured JSON responses."
        ),
        "machine learning": (
            "Build a machine learning prediction project "
            "with model evaluation and performance metrics."
        )
    }

    # Normalize skill names
    def normalize_skill(skill):
        return str(skill).strip().lower()

    def display_skill(skill):
        normalized = normalize_skill(skill)
        return skill_names.get(normalized, normalized.title())

    missing_skills = skill_gap_analysis.get("missing_skills", [])
    matched_skills = skill_gap_analysis.get("matched_skills", [])

    recommendations = []
    priority_actions = []
    project_suggestions = []
    learning_priorities = []

    # 1. Analyze missing skills
    for item in missing_skills:

        if isinstance(item, dict):
            skill = item.get("skill", "")
            priority = item.get("priority", "optional").lower()
        else:
            skill = str(item)
            priority = "optional"

        if not skill:
            continue

        normalized = normalize_skill(skill)
        professional_name = display_skill(skill)

        if priority == "critical":
            priority_actions.append(
                f"High priority: Gain practical experience in "
                f"{professional_name} through a hands-on project."
            )

            learning_priorities.append(
                f"Critical: Learn {professional_name} and "
                f"demonstrate it through a working application."
            )

        elif priority == "important":
            learning_priorities.append(
                f"Important: Strengthen your knowledge of "
                f"{professional_name} with practical exercises."
            )

        else:
            learning_priorities.append(
                f"Optional: Explore {professional_name} "
                f"to strengthen your technical profile."
            )

        recommendations.append(
            f"After gaining practical experience, add "
            f"{professional_name} to your resume with a "
            f"relevant project example."
        )

        # Generate skill-specific project suggestions
        if normalized in project_ideas:
            project_suggestions.append(project_ideas[normalized])

    # 2. Analyze existing skills
    if matched_skills:
        recommendations.append(
            "Highlight your matching technical skills in your "
            "professional summary, experience and project sections."
        )

        recommendations.append(
            "Explain how you used your existing technical skills "
            "to solve practical business or technical problems."
        )

    # 3. Improve professional experience section
    experience = resume_details.get("experience", "")

    if not experience:
        recommendations.append(
            "Add relevant professional experience, internships "
            "or practical project work with clear descriptions."
        )

    # 4. Improve resume impact
    recommendations.append(
        "Use measurable achievements such as processing time "
        "reduced, accuracy improved or API response time optimized."
    )

    recommendations.append(
        "Include relevant technologies, tools and implementation "
        "details in your project descriptions."
    )

    recommendations.append(
        "Use action-oriented statements such as Developed, "
        "Implemented, Automated and Optimized."
    )

    # 5. Remove duplicate recommendations
    recommendations = list(dict.fromkeys(recommendations))
    priority_actions = list(dict.fromkeys(priority_actions))
    project_suggestions = list(dict.fromkeys(project_suggestions))
    learning_priorities = list(dict.fromkeys(learning_priorities))

    # 6. Generate final report
    return {
        "priority_actions": priority_actions,
        "learning_priorities": learning_priorities,
        "resume_recommendations": recommendations,
        "project_suggestions": project_suggestions,
        "matched_skill_count": len(matched_skills),
        "missing_skill_count": len(missing_skills),
        "next_action": (
            "Start with critical missing skills, build practical "
            "projects and update your resume with verified evidence."
            if missing_skills
            else
            "Your technical skill coverage is strong. Focus on "
            "measurable achievements and project presentation."
        )
    }

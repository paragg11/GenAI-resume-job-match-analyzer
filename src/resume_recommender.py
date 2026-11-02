
def generate_resume_recommendations(
    resume_details,
    job_details,
    skill_gap_analysis
):
    """
    Generate personalized resume improvement recommendations.
    """

    resume_skills = [
        skill.lower()
        for skill in resume_details.get("skills", [])
    ]

    missing_skills = skill_gap_analysis.get(
        "missing_skills", []
    )

    matched_skills = skill_gap_analysis.get(
        "matched_skills", []
    )

    recommendations = []
    project_suggestions = []
    priority_actions = []

    # 1. Analyze missing skills
    for item in missing_skills:

        skill = item["skill"]
        priority = item["priority"]

        if priority == "critical":
            priority_actions.append(
                f"High priority: Develop practical experience in {skill}."
            )

        recommendations.append(
            f"Add {skill} to your skill set after gaining "
            f"practical experience."
        )

    # 2. Analyze existing skills
    if matched_skills:
        recommendations.append(
            "Highlight your matching technical skills "
            "in the professional summary and experience sections."
        )

    # 3. Identify project opportunities
    for item in missing_skills:

        skill = item["skill"]

        if skill in [
            "rag", "langchain", "llm",
            "embeddings", "vector databases"
        ]:
            project_suggestions.append(
                "Build a RAG-based application using "
                "LangChain, embeddings and vector databases."
            )

        elif skill in ["machine learning", "transformers", "nlp"]:
            project_suggestions.append(
                "Build an NLP or machine learning project "
                "to demonstrate practical experience."
            )

        elif skill in ["aws", "docker"]:
            project_suggestions.append(
                f"Create a deployment project demonstrating {skill}."
            )

        elif skill == "fastapi":
            project_suggestions.append(
                "Build a REST API using FastAPI."
            )

    # 4. Resume content improvements
    experience = resume_details.get("experience", "")

    if not experience:
        recommendations.append(
            "Add clear professional experience with measurable achievements."
        )

    recommendations.append(
        "Use measurable project outcomes instead of generic responsibilities."
    )

    recommendations.append(
        "Include relevant technical tools and technologies "
        "in your project descriptions."
    )

    # Remove duplicate project suggestions
    project_suggestions = list(dict.fromkeys(project_suggestions))

    # 5. Generate final report
    return {
        "priority_actions": priority_actions,
        "resume_recommendations": recommendations,
        "project_suggestions": project_suggestions,
        "matched_skill_count": len(matched_skills),
        "missing_skill_count": len(missing_skills),
        "next_action": (
            "Focus on critical missing skills and demonstrate "
            "them through practical projects."
            if missing_skills
            else "Your technical skill coverage is strong. "
                 "Focus on improving project descriptions and achievements."
        )
    }

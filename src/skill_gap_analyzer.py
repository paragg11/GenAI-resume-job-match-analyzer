
# Step 8: Advanced Skill Gap Analysis

# Define skill importance and weights
SKILL_WEIGHTS = {
    "critical": {
        "python": 3,
        "rag": 3,
        "langchain": 3,
        "machine learning": 3,
        "llm": 3,
        "vector databases": 3,
        "transformers": 3
    },
    "important": {
        "sql": 2,
        "aws": 2,
        "fastapi": 2,
        "nlp": 2,
        "embeddings": 2,
        "flask": 2,
        "pandas": 2
    },
    "optional": {
        "git": 1,
        "docker": 1,
        "rest api": 1,
        "excel": 1
    }
}

# Handle common alternative skill names
SKILL_ALIASES = {
    "retrieval augmented generation": "rag",
    "amazon web services": "aws",
    "vector database": "vector databases",
    "large language model": "llm",
    "large language models": "llm"
}


def normalize_skill(skill):
    """Standardize skill names."""
    skill = skill.lower().strip()
    return SKILL_ALIASES.get(skill, skill)


def get_skill_priority(skill):
    """Return priority and weight for a skill."""

    for priority, skills in SKILL_WEIGHTS.items():
        if skill in skills:
            return priority, skills[skill]

    # Unknown skills receive medium priority by default
    return "important", 2


def analyze_skill_gaps(required_skills, resume_skills):

    # Normalize and remove duplicate skills
    required_skills = list(
        dict.fromkeys(normalize_skill(s) for s in required_skills)
    )

    resume_skills = set(
        normalize_skill(s) for s in resume_skills
    )

    matched_skills = []
    missing_skills = []

    total_weight = 0
    matched_weight = 0

    # Compare required skills against resume skills
    for skill in required_skills:

        priority, weight = get_skill_priority(skill)

        total_weight += weight

        if skill in resume_skills:

            matched_skills.append({
                "skill": skill,
                "priority": priority,
                "weight": weight
            })

            matched_weight += weight

        else:

            missing_skills.append({
                "skill": skill,
                "priority": priority,
                "weight": weight
            })

    # Calculate weighted coverage
    coverage_score = (
        round((matched_weight / total_weight) * 100, 2)
        if total_weight > 0 else 0
    )

    # Sort missing skills by importance
    priority_order = {
        "critical": 1,
        "important": 2,
        "optional": 3
    }

    missing_skills.sort(
        key=lambda item: priority_order[item["priority"]]
    )

    # Generate learning recommendations
    recommendations = [
        f"Learn {item['skill']} ({item['priority']} priority)"
        for item in missing_skills
    ]

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_required_skills": len(required_skills),
        "matched_count": len(matched_skills),
        "missing_count": len(missing_skills),
        "weighted_coverage": coverage_score,
        "recommendations": recommendations
    }

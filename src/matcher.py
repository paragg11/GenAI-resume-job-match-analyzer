
def calculate_match(resume_details, job_details):

    resume_skills = {
        skill.lower()
        for skill in resume_details["skills"]
    }

    job_skills = {
        skill.lower()
        for skill in job_details["required_skills"]
    }

    matched_skills = resume_skills.intersection(job_skills)

    missing_skills = job_skills.difference(resume_skills)

    total_skills = len(job_skills)

    match_percentage = (
        len(matched_skills) / total_skills * 100
        if total_skills else 0
    )

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "total_required_skills": total_skills
    }

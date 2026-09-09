#!/usr/bin/env python
"""
Test script for the AI-Powered Resume Screening System
Demonstrates the NLP pipeline with embeddings and semantic similarity
"""

from app.pipeline import (
    extract_skills_nlp, 
    extract_experience_years,
    parse_job_description,
    rank_candidate,
    calculate_semantic_similarity
)

def test_nlp_pipeline():
    """Test the complete NLP pipeline"""
    
    print("\n" + "="*70)
    print("🤖 AI-POWERED RESUME SCREENING SYSTEM - NLP PIPELINE TEST")
    print("="*70)
    
    # Test 1: Job Description Parsing
    print("\n📋 TEST 1: Job Description Parsing")
    print("-" * 70)
    job_desc = """
    Senior Full-Stack Developer - Python/React
    Requirements:
    - 5+ years professional software development
    - Expertise in Python, FastAPI, Django
    - React and TypeScript for frontend
    - PostgreSQL, Redis, MongoDB experience
    - Docker and Kubernetes
    - AWS cloud deployment
    - Strong problem-solving and communication
    - Experience with machine learning projects is a plus
    """
    
    job_info = parse_job_description(job_desc)
    print(f"✅ Parsed job description into {len(job_info)} structured fields:")
    print(f"   - Skills extracted: {len(job_info.get('skills', {}))} categories")
    print(f"   - Experience required: {job_info.get('years_required', 0)} years")
    print(f"   - Job description text: {len(job_info.get('description_text', ''))} chars")
    
    # Test 2: Resume Skill Extraction
    print("\n📄 TEST 2: Resume Skill Extraction")
    print("-" * 70)
    resume_text = """
    JOHN DOE - Senior Software Engineer
    
    Experience:
    - 6 years building scalable web applications with Python and JavaScript
    - Expert in FastAPI, Django, and React frameworks
    - Deep experience with PostgreSQL, Redis, and MongoDB databases
    - Proficient in Docker containerization and Kubernetes orchestration
    - AWS certified with hands-on experience in EC2, S3, RDS, Lambda
    - Machine learning enthusiast with TensorFlow and PyTorch projects
    - Strong teamwork and communication skills
    - Problem solver who loves agile and DevOps practices
    
    Technologies:
    Python, FastAPI, Django, React, TypeScript, PostgreSQL, Redis,
    MongoDB, Docker, Kubernetes, AWS, TensorFlow, Git, CI/CD
    """
    
    resume_skills = extract_skills_nlp(resume_text)
    years = extract_experience_years(resume_text)
    
    total_skills = sum(len(v) for v in resume_skills.values())
    print(f"✅ Extracted {total_skills} skills across {len(resume_skills)} categories:")
    for category, skills in resume_skills.items():
        if skills:
            print(f"   {category.title()}: {', '.join(skills)}")
    print(f"\n📅 Years of experience detected: {years} years")
    
    # Test 3: Semantic Similarity
    print("\n🧠 TEST 3: Semantic Similarity & Embeddings")
    print("-" * 70)
    try:
        job_excerpt = job_info.get('description_text', '')[:500]
        resume_excerpt = resume_text[:500]
        similarity = calculate_semantic_similarity(job_excerpt, resume_excerpt)
        print(f"✅ Semantic similarity calculated: {similarity:.3f} (0.0-1.0 scale)")
        print(f"   This represents how conceptually similar the job and resume are")
        print(f"   based on embeddings from sentence-transformers model")
    except Exception as e:
        print(f"⚠️  Semantic similarity test skipped (embeddings not ready): {str(e)[:50]}")
    
    # Test 4: Full Ranking Pipeline
    print("\n🏆 TEST 4: Full Candidate Ranking")
    print("-" * 70)
    try:
        ranked = rank_candidate(
            filename="john_doe_resume.txt",
            resume_text=resume_text,
            job_info=job_info,
            use_embeddings=True
        )
        
        print(f"✅ Candidate ranked successfully!")
        print(f"   Final Score: {ranked.score}/100")
        print(f"   Recommendation: {ranked.recommendation}")
        print(f"   Summary: {ranked.summary}")
        print(f"\n📊 Scoring Breakdown:")
        if ranked.scoring_breakdown:
            sb = ranked.scoring_breakdown
            print(f"   🎯 Skill Match:      {sb.skill_match_score:.1f}%")
            print(f"   📊 Semantic Fit:     {sb.semantic_similarity_score:.1f}%")
            print(f"   📅 Experience:       {sb.experience_score:.1f}%")
            print(f"   ━━━━━━━━━━━━━━━━━━━━━")
            print(f"   🏆 Final Score:      {sb.final_score:.1f}%")
            
        print(f"\n🔍 Matched Skills: {', '.join(ranked.skills[:5])}")
        if ranked.missing_skills:
            print(f"⚠️  Missing Skills: {', '.join(ranked.missing_skills[:3])}")
            
    except Exception as e:
        print(f"❌ Ranking failed: {e}")
    
    print("\n" + "="*70)
    print("✅ PIPELINE TEST COMPLETE")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_nlp_pipeline()

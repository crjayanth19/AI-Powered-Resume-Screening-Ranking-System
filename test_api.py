#!/usr/bin/env python
"""Test the web API endpoint"""
import httpx

# Test the screening endpoint
job_description = """
Senior Full-Stack Developer Position
Required Skills:
- 5+ years Python development
- FastAPI or Django experience  
- React and TypeScript frontend
- PostgreSQL database expertise
- Docker and Kubernetes
- AWS cloud services
- Leadership and communication
- Agile/Scrum methodology

Experience:
Seeking someone with strong problem-solving abilities and proven track record 
in building scalable microservices. Must communicate clearly with team and
stakeholders. Machine learning experience is a nice-to-have.
"""

# Read test resume
with open('test_resume.txt', 'r') as f:
    resume_content = f.read()

# Prepare form data for multipart upload
files = {
    'resumes': ('test_resume.txt', resume_content, 'text/plain'),
}
data = {
    'job_description': job_description,
}

# Make the POST request
print("\n📤 Sending API request to /screening endpoint...")
try:
    response = httpx.post(
        'http://127.0.0.1:8000/screening',
        data=data,
        files=files,
        timeout=30.0
    )
    
    print(f"✅ Response Status: {response.status_code}")
    
    if response.status_code == 200:
        # Check if response contains HTML
        if '<html' in response.text.lower():
            print("✅ HTML response received")
            
            # Look for ranking in HTML
            if 'ranked candidates' in response.text.lower():
                print("✅ Rankings found in response")
                
                # Extract score if present
                if '/100' in response.text:
                    import re
                    scores = re.findall(r'(\d+)/100', response.text)
                    if scores:
                        print(f"🏆 Candidate Score: {scores[0]}/100")
                        
            # Check for scoring breakdown
            if 'breakdown' in response.text:
                print("✅ Scoring breakdown rendered in HTML")
                
        print("\n📊 Response preview (first 500 chars):")
        print(response.text[:500])
        
    else:
        print(f"❌ Unexpected status code: {response.status_code}")
        print(response.text[:500])
        
except Exception as e:
    print(f"❌ Error: {e}")

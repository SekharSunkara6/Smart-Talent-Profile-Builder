import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def gpt_extract_skills(resume_text):
    prompt = f"Extract the skills from this resume text: {resume_text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    skills_text = response.choices[0].message.content
    skills = [skill.strip() for skill in skills_text.split(',')]
    return skills

import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def gpt_generate_bio(work_samples):
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': f"Summarize this creator's work: {work_samples}"}]
    )
    return response.choices[0].message.content

def gpt_generate_hashtags(profile):
    skills = ', '.join(profile.get('skills', []))
    prompt = f"Generate 5 creative hashtags for an artist with skills {skills} and bio '{profile.get('bio','')}'"
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    hashtags_text = response.choices[0].message.content
    tags = [tag.strip() for tag in hashtags_text.split('#') if tag.strip()]
    return tags

def gpt_extract_skills(resume_text):
    prompt = f"Extract the skills from this resume text: {resume_text}"
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    skills_text = response.choices[0].message.content
    skills = [skill.strip() for skill in skills_text.split(',')]
    return skills

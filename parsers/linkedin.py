def parse_linkedin_profile(url=None, mocked_json=None):
    if mocked_json:
        data = mocked_json  # Dict with profile info
    else:
        # Scraping real LinkedIn is not recommended; use mocked data!
        data = {}
    name = data.get('name', '')
    bio = data.get('summary', '')
    skills = data.get('skills', [])
    location = data.get('location', '')
    return {'name': name, 'bio': bio, 'skills': skills, 'location': location, 'work_samples': [], 'categories': [], 'links': [url] if url else [], 'tags': []}

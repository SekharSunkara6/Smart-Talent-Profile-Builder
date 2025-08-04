import requests
from bs4 import BeautifulSoup

def parse_instagram_profile(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    name = soup.title.text.split('•')[0].strip()
    bio_tag = soup.find('meta', {'property':'og:description'})
    bio = bio_tag['content'].split('-')[0] if bio_tag else ''
    return {'name': name, 'bio': bio, 'work_samples': [], 'skills': [], 'categories': [], 'links': [url], 'tags': []}

# Later: Enhance work samples/tags using Instagram media (AI add-on)

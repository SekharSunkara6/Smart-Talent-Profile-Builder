from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class WorkSample(BaseModel):
    title: Optional[str] = None
    url: Optional[HttpUrl] = None
    tags: List[str] = []
    media_type: Optional[str] = None

class TalentProfile(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    bio: Optional[str] = None
    skills: List[str] = []
    categories: List[str] = []
    links: List[HttpUrl] = []
    work_samples: List[WorkSample] = []
    tags: List[str] = []
    enriched_bio: Optional[str] = None
    generated_hashtags: Optional[List[str]] = []
    ai_detected_skills: Optional[List[str]] = []
    voice_intro_transcript: Optional[str] = None

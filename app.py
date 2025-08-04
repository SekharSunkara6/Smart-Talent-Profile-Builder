from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env
load_dotenv()
print("Loaded OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("OPENAI_API_KEY is set:", bool(os.getenv("OPENAI_API_KEY")))  # Debug print

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

from typing import Dict, Any
from models import TalentProfile
from parsers import aggregate_profile_sources
from ai_utils.gpt import gpt_generate_bio, gpt_generate_hashtags
from ai_utils.skill_extraction import gpt_extract_skills
from ai_utils.whisper_transcribe import whisper_transcribe

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production usage as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

profiles = []
PROFILES_FILE = 'data/profiles.json'

def save_profiles():
    with open(PROFILES_FILE, 'w', encoding='utf-8') as f:
        json.dump(profiles, f, indent=2)

def load_profiles():
    global profiles
    if os.path.exists(PROFILES_FILE):
        with open(PROFILES_FILE, 'r', encoding='utf-8') as f:
            profiles = json.load(f)
    else:
        profiles = []

load_profiles()

@app.get("/")
def read_root():
    return {"message": "Smart Talent Profile Builder API is running successfully!"}

@app.post('/import_profile')
async def import_profile(payload: Dict[str, Any]):
    try:
        data = payload
        base_profile = aggregate_profile_sources(data)

        # Set defaults for missing fields to avoid validation errors
        defaults = {
            "location": None,
            "bio": None,
            "enriched_bio": None,
            "generated_hashtags": [],
            "ai_detected_skills": [],
            "voice_intro_transcript": None,
            "categories": [],
            "skills": [],
            "links": [],
            "work_samples": [],
            "tags": []
        }
        for key, val in defaults.items():
            base_profile.setdefault(key, val)

        # Enable AI enrichment with error handling
        try:
            if base_profile.get("work_samples"):
                base_profile["enriched_bio"] = gpt_generate_bio(str(base_profile["work_samples"]))
            else:
                base_profile["enriched_bio"] = gpt_generate_bio(base_profile.get("bio", ""))
        except Exception as e:
            base_profile["enriched_bio"] = None

        try:
            base_profile["generated_hashtags"] = gpt_generate_hashtags(base_profile)
        except Exception as e:
            base_profile["generated_hashtags"] = []

        try:
            resume_text = data.get("resume_text")
            if resume_text:
                base_profile["ai_detected_skills"] = gpt_extract_skills(resume_text)
        except Exception as e:
            base_profile["ai_detected_skills"] = []

        profile_obj = TalentProfile(**base_profile)
        json_profile = jsonable_encoder(profile_obj)  # Convert for JSON serialization

        profiles.append(json_profile)
        save_profiles()

        return JSONResponse(content={"profile": json_profile})
    except Exception as e:
        return {"error": str(e)}

@app.get('/profiles')
def get_profiles():
    load_profiles()
    return {"profiles": profiles}

@app.post('/upload_audio')
async def upload_audio(file: UploadFile = File(...)):
    if not os.path.exists("static"):
        os.makedirs("static")

    file_location = f"static/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    try:
        transcript = whisper_transcribe(file_location)
    except Exception as e:
        return {"transcript": f"Transcription failed: {str(e)}\nMock transcript: transcription temporarily disabled due to quota or API issues."}

    return {"transcript": transcript}

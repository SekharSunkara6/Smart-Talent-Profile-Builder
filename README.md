# Smart Talent Profile Builder API

Live URL: https://smart-talent-profile-builder.onrender.com/docs

---

## Overview

Smart Talent Profile Builder is a backend API service designed to automate onboarding and profile creation for creators and talent (photographers, designers, videographers, writers, artists, directors, and more). It ingests data from multiple external sources (Instagram, LinkedIn mock data, resumes) and automatically builds rich, structured, searchable profiles enhanced with AI.

This system drastically reduces manual onboarding effort, improves profile quality, and helps in effective talent matchmaking inside platforms like BreadButter.

---

## Features

### Core

- Import creator data from at least two sources — Instagram link and LinkedIn mock JSON, plus resume text.
- Parse, clean, and store diverse content: personal info, skills, work samples, links, tags.
- Scalable Pydantic schemas modeling profiles, work samples, hashtags, voice intros.
- REST API backend with FastAPI, documented and testable via OpenAPI Swagger UI.

### Optional AI Add-ons

- **AI-enhanced profile enrichment:** Generate bios, hashtags, summaries with OpenAI GPT.
- **Skills and categories auto-detection:** Automatically extract skills from resumes and links.
- **Voice intro transcription:** Upload audio intros transcribed with Whisper model.
- **Graceful fallback:** When your OpenAI API quota is exceeded, the system returns mock data and safe defaults—ensuring total uptime without errors.
- Placeholder hooks for future image/video tagging AI models for enhancing work samples.

---

## Live API URLs

| Endpoint               | Method | Description                                        |
|------------------------|--------|----------------------------------------------------|
| `/`                    | GET    | Health check — confirms API is running             |
| `/import_profile`       | POST   | Import and build profile from JSON sources         |
| `/profiles`             | GET    | List all stored profiles                            |
| `/upload_audio`         | POST   | Upload audio file for transcription (Whisper AI)  |

**Try it now:** [Swagger UI Documentation](https://smart-talent-profile-builder.onrender.com/docs)

---

## Usage Examples

### Import Profile Sample Request (POST `/import_profile`)

```
{
  "linkedin_mock": {
    "name": "Diya Singh",
    "summary": "Fashion photographer from Mumbai with 7 years experience.",
    "skills": ["photography", "editing", "branding"],
    "location": "Mumbai, India"
  },
  "instagram_url": "https://instagram.com/somepublicprofile",
  "resume_text": "Experienced in portrait and commercial photography, Adobe Lightroom, studio lighting.",
  "work_samples": [],
  "links": []
}
```

### Upload Audio (POST `/upload_audio`)

Use multipart/form-data with a valid audio file (e.g., `.mp3`).

Sample cURL:

```
curl -X POST "https://smart-talent-profile-builder.onrender.com/upload_audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path_to_audio_file.mp3"
```

---

## Setup & Deployment

### Local Setup

1. Clone the repo.

2. Create a Python 3.10 virtual environment:

   ```
   python3.10 -m venv venv
   source venv/bin/activate  # Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key in environment variables:

   ```
   export OPENAI_API_KEY="your_openai_api_key"  # Windows PowerShell: $env:OPENAI_API_KEY="your_key"
   ```

5. Run the app locally:

   ```
   uvicorn app:app --reload
   ```

---

### Production Deployment

- Hosted on Render at: https://smart-talent-profile-builder.onrender.com
- **Python version fixed as 3.10 via runtime.txt and environment variable on Render**
- Environment variable `OPENAI_API_KEY` set securely on Render dashboard
- Auto deployment enabled on GitHub push

---

## Important Notes on OpenAI Quota and AI Features

- The API heavily relies on OpenAI GPT and Whisper models for bios, hashtags, skills detection, and transcription.
- **If your OpenAI API quota is exceeded or billing is not enabled, the system gracefully returns mock data and fallback messages instead of failing.**
- For full AI-powered profile enrichment and voice transcription, ensure your OpenAI subscription and billing are active, and your quota allows sufficient usage.
- You can monitor API usage and quota on your [OpenAI dashboard](https://platform.openai.com/account/usage).

---

## Project Structure

```
├── ai_utils/
│   ├── gpt.py                # OpenAI GPT helpers (bio, hashtags, skills)
│   ├── whisper_transcribe.py # Whisper audio transcription code
│   └── ...                   # Other AI utilities
├── parsers/
│   ├── instagram.py          # Instagram profile parser
│   ├── linkedin.py           # LinkedIn JSON parser/mock
│   └── ...
├── data/
│   └── profiles.json         # Stored profiles data (tracked in Git)
├── app.py                    # FastAPI app with endpoints
├── models.py                 # Pydantic models for profiles
├── requirements.txt          # Pinned Python dependencies
├── runtime.txt               # Python version for Render (python-3.10.14)
├── .env (ignored)            # Local environment variables (not pushed)
└── README.md                 # This file
```

---

## FAQ

**Q: What happens when OpenAI quota is exceeded?**  
A: The API returns safe fallback mock data and does not interrupt your UX, ensuring uptime.

**Q: How can I add new AI integrations like image tagging?**  
A: The project has placeholder AI utility modules — you can extend them easily with new API calls.

**Q: Can I deploy this on other platforms?**  
A: Yes, with Python 3.10 and configured environment variables, you can deploy on AWS, Heroku, or similar.

---

## Contributors

- [Sekhar Sunkara](https://github.com/SekharSunkara6) — Backend & AI developer, project lead.
Thank you for using Smart Talent Profile Builder!  
Create better profiles with less effort and smarter automation!

---

*This project is built with FastAPI, OpenAI GPT & Whisper, and hosted on Render.*
```

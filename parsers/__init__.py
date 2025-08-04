from .instagram import parse_instagram_profile
from .linkedin import parse_linkedin_profile

def aggregate_profile_sources(data):
    profile = {}
    if "instagram_url" in data:
        insta = parse_instagram_profile(data["instagram_url"])
        profile.update(insta)
    if "linkedin_mock" in data:
        linked = parse_linkedin_profile(mocked_json=data["linkedin_mock"])
        for k, v in linked.items():
            if isinstance(v, list):
                profile[k] = list(set((profile.get(k) or []) + v))
            elif v and not profile.get(k):
                profile[k] = v
    profile.setdefault("skills", [])
    profile.setdefault("links", [])
    profile.setdefault("tags", [])
    profile.setdefault("work_samples", [])
    profile.setdefault("categories", [])
    return profile

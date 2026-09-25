import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not SERPAPI_KEY:
    raise ValueError("Serpapi key is missing check your .env file")


def get_trending_keywords(topic="artificial intelligence"):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_trends",
        "q": topic,
        "hl": "en",
        "date": "today 12-m",
        "tz": "420",
        "data_type": "RELATED_QUERIES",
        "api_key": SERPAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("\n RAW RESPONSE:\n", data)

    if "related_queries" in data:
        keywords = [
            item["query"]
            for item in data["related_queries"]["top"][:10]
            if "ai" in item["query"].lower()
            or "artificial intelligence" in item["query"].lower()
        ]

        return keywords

    return []
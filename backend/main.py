from fastapi import FastAPI, Query 
from google_trends import get_trending_keywords 
from youtube_trends import get_youtube_trending_videos 
from groq import Groq 
import os 
from dotenv import load_dotenv 
 
load_dotenv() 
 
GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
 
if not GROQ_API_KEY: 
    raise ValueError("Groq API key is missing. Check your .env file") 
 
client = Groq(api_key=GROQ_API_KEY) 
 
app = FastAPI() 
 
@app.get("/generate_ideas/") 
def generate_video_ideas( 
    topic: str = Query(..., title="Topic"), 
    audience: str = Query("Beginners", title="Target Audience"), 
    region: str = Query("US", title="Region") 
): 
    trending_keywords = get_trending_keywords(topic) 
 
    if not trending_keywords: 
        trending_keywords = ["No trending keywords found for this topic"] 
    trending_videos = get_youtube_trending_videos(topic, region) 
 
    if not trending_videos: 
        trending_videos = [{"title": "No Trending Videos Found", "url": "#"}] 
 
    prompt = f""" 
    Generate 5 engaging YouTube video ideas on '{topic}' for '{audience}' that are currently trending. 
    Consider these trending keywords: {', '.join(trending_keywords)} 
    Use insights from these trending youtube videos: {', '.join([video['title'] for video in trending_videos])} 
    """ 
    try: 
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        ideas = response.choices[0].message.content.strip()
    except Exception as e: 
        ideas = f"Groq API Error: {str(e)}" 
 
    return { 
        "trending_keywords": trending_keywords, 
        "trending_videos": trending_videos, 
        "ideas": ideas 
    }
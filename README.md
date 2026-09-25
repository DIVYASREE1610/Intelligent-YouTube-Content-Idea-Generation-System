# Intelligent YouTube Content Idea Generator

An AI-powered content research assistant that helps creators discover trending topics and generate YouTube video ideas. The application combines Google Trends data, YouTube search results, and Groq-powered language generation in a simple Streamlit interface.

## Features

- Accepts a content topic, target audience, and YouTube region.
- Retrieves related search keywords through SerpAPI's Google Trends engine.
- Finds up to five relevant, high-view-count YouTube videos using the YouTube Data API.
- Generates five audience-specific video ideas with a Groq-hosted language model.
- Presents keywords, reference videos, and generated ideas in a Streamlit UI.
- Exposes the generation workflow through a FastAPI endpoint for easy integration.




## Project Structure

```text
Idea_Generator/
|
|-- backend/
|   |-- __init__.py          # Backend package marker
|   |-- app.py               # Streamlit frontend
|   |-- main.py              # FastAPI application and API route
|   |-- google_trends.py     # SerpAPI Google Trends integration
|   |-- youtube_trends.py    # YouTube Data API integration
|   |-- requirements.txt     # Python dependencies
|   
|-- .gitignore
`-- README.md
```

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | Streamlit |
| Backend API | FastAPI and Uvicorn |
| Trend research | SerpAPI Google Trends |
| Video research | YouTube Data API v3 |
| AI generation | Groq API |
| Language | Python |

## Prerequisites

- Python 3.10 or newer
- A SerpAPI key
- A YouTube Data API v3 key
- A Groq API key



Create `backend/.env` and add the required credentials:

	 SERPAPI_KEY=your_serpapi_key
	 YOUTUBE_API_KEY=your_youtube_data_api_key
	 GROQ_API_KEY=your_groq_api_key
	



## Run the Application

Start the FastAPI backend from the `backend` directory:

```bash
cd backend
uvicorn main:app --reload --port 8000
```

In a second terminal, from the project root, start the Streamlit frontend:

```bash
streamlit run backend/app.py
```

Open the URL displayed by Streamlit,

## How It Works

1. The user submits a topic, audience level, and region in Streamlit.
2. FastAPI requests related keywords from Google Trends through SerpAPI.
3. FastAPI searches YouTube for relevant videos and collects their titles and links.
4. The collected research is added to a prompt for the Groq model.
5. The API returns the research and generated ideas to the Streamlit frontend.



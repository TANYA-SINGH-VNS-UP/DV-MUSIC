import os
from googleapiclient.discovery import build

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def search_youtube(query):
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1,
        type="video"
    )
    response = request.execute()
    if not response["items"]:
        return None
    video_id = response["items"][0]["id"]["videoId"]
    return f"https://www.youtube.com/watch?v={video_id}"

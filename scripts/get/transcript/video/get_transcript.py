import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_id):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list_obj = ytt_api.list(video_id)
        
        # Prefer French or English
        try:
            transcript = transcript_list_obj.find_transcript(['en', 'en-US', 'en-GB','fr', 'fr-FR', 'fr-BE', 'fr-CA', 'fr-CH'])
        except:
            # Fallback to the first available if neither is found
            transcript = list(transcript_list_obj)[0]
        
        transcript_data = transcript.fetch()
        
        # The data returned by fetch() can be a list of dicts (old API) 
        # or a FetchedTranscript object (new API version)
        if hasattr(transcript_data, 'snippets'):
            text = " ".join([snippet.text for snippet in transcript_data.snippets])
        else:
            text = " ".join([item['text'] for item in transcript_data])
            
        return text

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_id = sys.argv[1]
        print(get_youtube_transcript(video_id))
    else:
        print("Usage: python get_transcript.py <video_id>")
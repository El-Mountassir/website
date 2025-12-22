import sys
import re
import argparse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, SRTFormatter, JSONFormatter

def extract_video_id(url_or_id):
    """
    Extracts the video ID from a YouTube URL or returns the ID if provided directly.
    """
    # Regex to handle various YouTube URL formats (standard, short, embed)
    regex = r"(?:v=|/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url_or_id)
    if match:
        return match.group(1)
    return url_or_id

def get_formatter(format_type):
    if format_type == 'json':
        return JSONFormatter()
    elif format_type == 'srt':
        return SRTFormatter()
    else:
        return TextFormatter()

def get_youtube_transcript(video_input, languages=None, output_format='text'):
    video_id = extract_video_id(video_input)
    
    # Default priority: French, then English
    if not languages:
        languages = ['fr', 'fr-FR', 'fr-BE', 'fr-CA', 'fr-CH', 'en', 'en-US', 'en-GB']

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list_obj = ytt_api.list(video_id)
        
        try:
            transcript = transcript_list_obj.find_transcript(languages)
        except:
            # Fallback to the first available if preferred languages are not found
            # We explicitly fetch the first one available
            transcript = transcript_list_obj.find_transcript([t.language_code for t in transcript_list_obj])

        transcript_data = transcript.fetch()
        
        # Use the official formatters for cleaner output
        formatter = get_formatter(output_format)
        formatted_output = formatter.format_transcript(transcript_data)
            
        return formatted_output

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch YouTube video transcripts.")
    parser.add_argument("video", help="Video ID or full YouTube URL")
    parser.add_argument("-l", "--lang", nargs="+", help="Preferred languages codes (e.g. fr en)")
    parser.add_argument("-f", "--format", choices=['text', 'json', 'srt'], default='text', help="Output format (default: text)")
    parser.add_argument("-o", "--output", help="Output file path (optional)")

    args = parser.parse_args()

    content = get_youtube_transcript(args.video, args.lang, args.format)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Transcript saved to {args.output}")
    else:
        print(content)

import yt_dlp

def download_youtube_video(url):
    # yt-dlp options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Select best video and audio streams
        'outtmpl': '%(title)s.%(ext)s',        # Save the file with the video title as filename
        'postprocessors': [{                  # Merge audio and video after download (if needed)
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',         # Ensure it's in MP4 format
        }],
        'merge_output_format': 'mp4',          # Force final output as MP4
        'progress_hooks': [hook],              # Optional: Show progress during download
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def hook(d):
    """This function is called during the download process to show progress."""
    if d['status'] == 'downloading':
        print(f"Downloading... {d['_percent_str']} at {d['_speed_str']}")
    elif d['status'] == 'finished':
        print(f"Download finished: {d['filename']}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")  # Prompt for YouTube URL
    download_youtube_video(video_url)  # Download the video

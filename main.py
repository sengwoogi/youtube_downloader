import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError

def download_media(youtube_url, download_format):
    """
    Downloads a video or audio from YouTube.

    Args:
        youtube_url (str): The URL of the YouTube video.
        download_format (str): The format to download, either 'mp4' or 'mp3'.
    """
    try:
        yt = YouTube(youtube_url)

        if download_format == 'mp4':
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if stream:
                stream.download()
                print(f"Successfully downloaded: {stream.default_filename}")
            else:
                print("No suitable mp4 stream found.")
        elif download_format == 'mp3':
            stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            if stream:
                outfile = stream.download()
                base, ext = os.path.splitext(outfile)
                new_file = base + '.mp3'
                os.rename(outfile, new_file)
                print(f"Successfully downloaded and converted to mp3: {new_file}")
            else:
                print("No suitable audio stream found.")
        else:
            print("Invalid download format. Please choose 'mp4' or 'mp3'.")

    except VideoUnavailable:
        print(f"Error: Video {youtube_url} is unavailable.")
    except RegexMatchError:
        print(f"Error: Could not parse YouTube URL: {youtube_url}. Please check the URL.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    youtube_url = input("Enter the YouTube video URL: ")

    while True:
        download_format = input("Choose download format ('mp3' or 'mp4'): ").lower()
        if download_format in ['mp3', 'mp4']:
            break
        else:
            print("Invalid format. Please enter 'mp3' or 'mp4'.")

    download_media(youtube_url, download_format)

import yt_dlp
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            percent = downloaded / total * 100
            bar_len = 30
            filled_len = int(bar_len * percent // 100)
            bar = '█' * filled_len + '-' * (bar_len - filled_len)
            print(f"\r[Download] |{bar}| {percent:5.1f}%", end='')
    elif d['status'] == 'finished':
        print("\r[Download] |██████████████████████████████| 100.0% Done!")

def download_video(url, ydl_opts):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print("\nTitle:", info.get('title', 'No Title'))
            print("Views:", info.get('view_count', 'Unknown'))
            print("Duration:", info.get('duration', 'Unknown'), "seconds")
            print("\nDownloading...")
            ydl.download([url])
        print("\nDownload completed!")
        print("Saved to:", os.getcwd())
    except Exception as e:
        print("\nAn error occurred:", str(e))

def main():
    url = input("Enter YouTube video URL: ")
    print("Select the format to download:")
    print("1. mp4 (video)")
    print("2. mp3 (audio)")
    fmt_choice = input("Enter the number (1 or 2): ")

    print("\nConverting, please wait...")

    # 병렬 fragment 다운로드 수
    concurrent_fragments = 16

    ydl_base_opts = {
        'quiet': True,  # 불필요한 출력 억제
        'no_warnings': True,
        'progress_hooks': [progress_hook],
    }

    if fmt_choice == '1':
        ydl_opts = {
            **ydl_base_opts,
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'concurrent_fragment_downloads': concurrent_fragments,
            'retries': 10,
            'fragment_retries': 10,
            'socket_timeout': 30,
        }
        file_type = 'mp4'
    elif fmt_choice == '2':
        ydl_opts = {
            **ydl_base_opts,
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'concurrent_fragment_downloads': concurrent_fragments,
            'retries': 10,
            'fragment_retries': 10,
            'socket_timeout': 30,
        }
        file_type = 'mp3'
    else:
        print("Invalid input. Exiting program.")
        return

    # 플레이리스트 여부 확인
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                # 플레이리스트: 여러 영상 병렬 다운로드
                entries = list(info['entries'])
                print(f"Playlist detected: {len(entries)} videos, downloading up to 4 in parallel.")
                with ThreadPoolExecutor(max_workers=4) as executor:
                    futures = [executor.submit(download_video, entry['webpage_url'], ydl_opts) for entry in entries]
                    for f in as_completed(futures):
                        pass
            else:
                # 단일 영상
                download_video(url, ydl_opts)
    except Exception as e:
        print("\nAn error occurred:", str(e))
        print("\nPlease check the following:")
        print("1. The URL is correct")
        print("2. The video is not private")
        print("3. Your internet connection is stable")
        print("4. The video does not have age restrictions")

if __name__ == "__main__":
    main()

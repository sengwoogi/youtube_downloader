# YouTube Downloader

A simple Python script to download YouTube videos as MP4 (video) or MP3 (audio-only) using `yt-dlp`.

**Key Features:**
*   Download videos as MP4 or audio as MP3.
*   Supports downloading entire playlists.
*   Utilizes parallel downloads for faster playlist processing.

## Prerequisites

**FFmpeg is required** for this script to function correctly, especially for:
*   Merging video and audio streams downloaded by `yt-dlp`.
*   Converting audio to MP3 format.

The `init_project.sh` script (for Linux/macOS users) will check if FFmpeg is installed and guide you if it's missing.

**Windows Users:** You will need to install FFmpeg manually and ensure it's added to your system's PATH.
*   Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
*   Follow instructions for your operating system to add the `bin` directory (containing `ffmpeg.exe`) to your PATH environment variable.

## Setup

1.  **Create and activate a Python virtual environment** of your choice (e.g., using `venv`, `conda`, `uv`).
    Example using `venv`:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    # .venv\Scripts\activate   # On Windows CMD
    # .venv\Scripts\Activate.ps1 # On Windows PowerShell
    ```

2.  **Install dependencies:**

    *   **For Linux/macOS users:**
        Run the initialization script. It will check for FFmpeg and install Python packages.
        ```bash
        chmod +x init_project.sh
        ./init_project.sh
        ```

    *   **For Windows users:**
        First, ensure FFmpeg is installed and accessible via your system's PATH (see Prerequisites).
        Then, install the Python packages:
        ```bash
        pip install -r requirements.txt
        ```
        (Or, if you use `uv`: `uv pip install -r requirements.txt`)

## Usage

1.  Make sure your virtual environment is activated and you have run the setup steps.
2.  Run the script from the project's root directory:
    ```bash
    python main.py
    ```
3.  The script will prompt you to enter the YouTube video or playlist URL and then ask you to choose the download format ('mp3' or 'mp4').
4.  Downloaded files will be saved in a `downloads` directory within the project folder. For playlists, multiple files will be downloaded.

## Note on MP3 Files

When you choose the 'mp3' format, `yt-dlp` attempts to download the best audio and convert it to MP3. This process relies on **FFmpeg** being installed and accessible to `yt-dlp`.

If FFmpeg is correctly installed and found by `yt-dlp`, you will get a proper MP3 file.
If FFmpeg is not found, `yt-dlp` might save the audio in a different format (e.g., m4a, opus) or the download/conversion process for MP3 might fail. Please ensure FFmpeg is installed as per the "Prerequisites" section.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is open source and available under the [MIT License](LICENSE).
(You would typically add a LICENSE file to your project)

# YouTube Downloader

A simple Python script to download YouTube videos as MP4 (video) or MP3 (audio-only).

## Setup

1.  **Create a virtual environment:**
    Open your terminal or command prompt in the project's root directory and run:
    ```bash
    uv venv .venv
    ```

2.  **Activate the virtual environment:**
    *   On **Linux/macOS**:
        ```bash
        source .venv/bin/activate
        ```
    *   On **Windows** (Command Prompt):
        ```bash
        .venv\Scripts\activate
        ```
    *   On **Windows** (PowerShell):
        ```powershell
        .venv\Scripts\Activate.ps1
        ```

3.  **Install dependencies:**
    Once the virtual environment is activated, install the required packages using:
    ```bash
    uv pip install -r requirements.txt
    ```
    *(Note: We will generate the `requirements.txt` file in a subsequent step.)*

## Usage

1.  Make sure your virtual environment is activated.
2.  Run the script from the project's root directory:
    ```bash
    python main.py
    ```
3.  The script will prompt you to enter the YouTube video URL and then ask you to choose the download format ('mp3' or 'mp4').
4.  The downloaded file will be saved in the same directory where the script is located.

## Note on MP3 Files

When you choose the 'mp3' format, the script downloads the best available audio-only stream (often in formats like WebM with Opus audio or M4A with AAC audio). It then renames the downloaded file to have an `.mp3` extension.

This means the resulting file is not a "true" MP3 encoded file but rather the original audio stream with its container changed. Most modern audio players can handle these files without any issues. However, if you require a strict MP3 file (e.g., for compatibility with older devices), you would need to use additional tools like FFmpeg to perform a full audio conversion. This script does not include FFmpeg integration.

#!/bin/bash

echo "Starting project setup..."

# Check for FFmpeg
if ! command -v ffmpeg &> /dev/null
then
    echo "FFmpeg is required but not found."
    echo "Please install FFmpeg using your system's package manager."
    echo "Example commands:"
    echo "  Debian/Ubuntu: sudo apt-get update && sudo apt-get install -y ffmpeg"
    echo "  Fedora/CentOS/RHEL: sudo yum install -y ffmpeg  # or sudo dnf install -y ffmpeg"
    exit 1
fi

echo "Installing Python dependencies..."
# Install Python dependencies
pip install -r requirements.txt
# Or, if you use uv: uv pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error installing Python dependencies. Please check the output above."
    exit 1
fi

echo "Project setup completed successfully!"

#!/bin/bash

# Function to install Python on Linux
install_python_linux() {
    echo "Python is not installed. Installing Python on Linux..."

    if command -v apt-get &>/dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip
    elif command -v yum &>/dev/null; then
        sudo yum install -y python3 python3-pip
    else
        echo "Unsupported Linux distribution. Please install Python manually."
        exit 1
    fi
}

# Function to install Python on macOS
install_python_mac() {
    echo "Python is not installed. Installing Python on macOS..."

    if command -v brew &>/dev/null; then
        brew install python
    else
        echo "Homebrew not found. Please install Homebrew first: https://brew.sh"
        exit 1
    fi
}

# Function to install Python on Windows
install_python_windows() {
    echo "Python is not installed. Installing Python on Windows..."

    # Download Python installer
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe

    # Run the installer
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

    # Remove the installer after installation
    rm python-installer.exe
}

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    # Detect the operating system
    case "$OSTYPE" in
        linux-gnu*) install_python_linux ;;
        darwin*) install_python_mac ;;
        msys* | cygwin* | win32*) install_python_windows ;;
        *) echo "Unsupported OS. Please install Python manually." ; exit 1 ;;
    esac
fi

# Check if pip (Python package manager) is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip is not installed. Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    rm get-pip.py
fi

# Install necessary Python packages
echo "Installing required Python packages..."
pip3 install pygame

echo "Setup completed successfully!"
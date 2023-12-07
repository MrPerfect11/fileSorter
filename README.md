# File Sorter
File Sorter is a Python script that organizes files in a specified directory based on their extensions. It creates a standalone executable, allowing users to run the program without opening a Python editor.

## Features

- **Organize Files:** Sorts files in the specified directory into folders based on their file extensions.
- **Organize Subfolders:** Option to organize files within subfolders recursively.
- **Executable:** Create a standalone executable for easy execution on any device.

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
1. **Create Executable: in terminal**
    ```bash
    python -m PyInstaller --onefile fileSorter.py
1. **Run Executable:**
    .\dist\fileSorter.exe **On Windows:**
    ./dist/fileSorter **On Linux/Mac:**
1. **Select Target Folder:**
    Choose the folder you want to organize when prompted.
1. **Options:**
    Choose whether to organize subfolders.
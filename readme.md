<h1 align = center>PITCH - Your Ultimate YouTube Audio Downloader 🎵</h1>

<p align="center">
  ![yt-dlp](https://img.shields.io/badge/yt--dlp-Downloader-blue?logo=yt-dlp&logoColor=white)
</p>

<p align="center">
  yt-dlp - A powerful tool for downloading videos and audio from YouTube and many other platforms.
</p>

<p align="center">
  ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
</p>

<p align="center">
  ![Windows](https://img.shields.io/badge/Windows-OS-0078D6?logo=windows&logoColor=white)
</p>

Welcome to **Pitch** – your personal YouTube audio downloader! With Pitch, you can easily download your favorite songs from YouTube and save them in your preferred format. It's simple to use and built to save your time with a clean and smooth experience.

---

### 🚀 Prerequisites:

Before running **Pitch**, ensure that you have the following installed and set up:

1. **Python 3.6+** installed on your system.
2. **Git** installed (if you are cloning the repository).

---

### 📥 Checking if Python is Installed And Working (IMPORTANT) :

To begin, ensure that Python is installed on your system and added to the environment variables:

1. Open the **Command Prompt (cmd)**.
2. Run the following command to check the Python version:

   ```bash
   python --version
   ```
   If python is installed correctly, You should see something like:
   ```bash
   python3.x.x

If not, Then python is not added to the PATH in environment Variables or not installed correctly

*To edit the PATH environment variable:*
- Right-click on This PC or Computer on your desktop or in File Explorer, and choose Properties.
- Click Advanced system settings on the left side.
- Click Environment Variables at the bottom of the System Properties window.
- Under System variables, scroll down and select the Path variable, then click Edit.
- In the Edit Environment Variable dialog, click New, then add the path to the Python directory (for example: C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python310).
- Also add the Scripts folder to the PATH: C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python310\Scripts.
---

### 🔧 Installation Steps:

1. Clone the Repository:
To clone the repository:
```bash
git clone https://github.com/Aneerudh17/Pitch-CLI.git
```
2. Run the Batch File:
```bash
./run.bat
```
This will install all the required dependencies and run the program.

---
### 📝 How to Use Pitch:
1. After running the batch file or executing the Python script, you'll see the Pitch intro and an ASCII art welcome message.
2. Enter the YouTube URL of the song you'd like to download.
3. Choose the location where you'd like to save the downloaded file.
4. Repeat the process to download more songs, or quit the program when you're done.
---
### ❓ How It Works:
Pitch works by downloading audio from YouTube videos using yt-dlp, an advanced fork of youtube-dl. The script extracts the audio from the video and saves it in a .webm format. You can later convert it to MP3 if you prefer, or leave it in the .webm format.

---
### 🧑‍💻 Contributions:
I welcome contributions to improve Pitch. Feel free to fork the repository, open issues, or submit pull requests. If you encounter any bugs or have ideas for new features, please let me know.

---
###
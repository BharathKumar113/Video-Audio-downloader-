#  Video & Audio Downloader  
![Python](https://img.shields.io/badge/Python-3.10-blue)

A sleek **Flask-powered web application** that lets you easily **download videos or extract audio** from YouTube links using [yt-dlp](https://github.com/yt-dlp/yt-dlp).  

 With just a link, you can choose between **high-quality video** or **MP3 audio**, and instantly save the file to your device.  

---

##  Why this project?  

 Most online downloaders are either filled with ads or unreliable.  
 This project gives you:  
-  **Full control** — run locally on your machine.  
-  **Faster & safer downloads** — thanks to `yt-dlp`.  
-  **Simple interface** — no extra distractions, just paste → download.  

Whether you want to **save tutorials, lectures, or music tracks**, this tool makes it quick and hassle-free.  

---

##  Features  

✔️ Download videos in the **best available quality**  
✔️ Extract audio as **high-quality MP3 (192 kbps)**  
✔️ Auto-organized **downloads folder**  
✔️ **Cross-platform** – works on Windows, macOS, and Linux  
✔️ Lightweight, just **Flask + yt-dlp**  
✔️ Clean and minimal **web UI**  

---

##  How it works  

1.  Paste a **YouTube URL** into the form.  
2.  Select whether you want **Video** or **Audio**.  
3.  App calls `yt-dlp` behind the scenes to fetch and process the media.  
4.  The file gets stored inside the `downloads/` folder.  
5.  You get a **direct download link** to save it locally.  

---

##  Project Structure  

```
 video-audio-downloader
 ┣  app.py             # Main Flask app
 ┣  templates
 ┃ ┗  index.html       # User interface
 ┣  downloads          # Auto-created download folder
 ┗  README.md          # Project documentation
```

---

##  Installation  

### 1. Clone the repo  
```bash
git clone https://github.com/BharathKumar113/Video-Audio-Downloader.git
cd Video-Audio-Downloader
```

### 2. (Optional) Create a virtual environment  
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies  
```bash
pip install -r requirements.txt
```

Or install directly:  
```bash
pip install flask yt-dlp
```

- For audio downloads, make sure you have **FFmpeg** installed:  
- On Linux: `sudo apt install ffmpeg`  
- On macOS (Homebrew): `brew install ffmpeg`  
- On Windows: [Download FFmpeg](https://ffmpeg.org/download.html)  

### 4. Run the application  
```bash
python app.py
```

Visit: **http://127.0.0.1:5000/** in your browser.  

---

##  Usage Guide  

1. Paste a YouTube video link  
2. Choose **Video** or **Audio (MP3)**  
3. Hit **Download** 
4. File is saved under `/downloads` and a direct link is provided  

---

##  Legal Note  

 This project is intended **for personal use only**.  
Downloading copyrighted content without permission may violate **YouTube’s Terms of Service**.  
Always ensure you have the rights to download the content.  

---



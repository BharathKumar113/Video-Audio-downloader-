from flask import Flask, render_template, request, send_from_directory
import os
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        download_type = request.form.get("type", "video")  # video or audio

        if not url:
            return render_template("index.html", error="Please enter a URL!")

        try:
            ydl_opts = {
                "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
                "quiet": True,
            }

            # If user wants audio only, set format and extension
            if download_type == "audio":
                ydl_opts.update({
                    "format": "bestaudio/best",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                })

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

                # If audio, rename to .mp3 manually since we might not have ffmpeg
                if download_type == "audio" and not filename.endswith(".mp3"):
                    mp3_filename = os.path.splitext(filename)[0] + ".mp3"
                    os.rename(filename, mp3_filename)
                    filename = mp3_filename

            return render_template("index.html", success=True, file=os.path.basename(filename))

        except Exception as e:
            return render_template("index.html", error=f"Error: {str(e)}")

    return render_template("index.html")

@app.route("/downloads/<filename>")
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

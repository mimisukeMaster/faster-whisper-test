from faster_whisper import WhisperModel
import subprocess
YOUTUBE_URL = "https://youtu.be/9GKo2iogPsM"
YOUTUBE_URL = YOUTUBE_URL.split("?")[0]
YOUTUBE_ID = YOUTUBE_URL.split("youtu.be/")[-1] # Youtube ID
AUDIO_FILE_NAME = f"{YOUTUBE_ID}.mp3"
# Download audio from Youtube
def dl_yt(yt_url):
    subprocess.run(f"yt-dlp -x --audio-format mp3 -o {AUDIO_FILE_NAME} {yt_url}", shell=True)

dl_yt(f"{YOUTUBE_URL}")

model = WhisperModel("small", device="cuda", compute_type="int8")

segments, info = model.transcribe(
	AUDIO_FILE_NAME,
	beam_size=8,
    log_prob_threshold=0,
    no_speech_threshold=1,
	vad_filter=False,
	without_timestamps=True,)
	
print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    
import os
os.remove(AUDIO_FILE_NAME) 
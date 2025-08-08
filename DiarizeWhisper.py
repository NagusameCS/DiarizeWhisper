import os
import tempfile
from pydub import AudioSegment
from pydub.utils import make_chunks
from pyannote.audio import Pipeline
import whisper

# SETTINGS
RECORDER_PATH = "INPUT/PATH/HERE"  # Change this to your device mount path
OUTPUT_PATH = "OUTPUT/PATH/HERE"  # Where transcripts will be saved
HF_TOKEN = "YOUR_KEY_HERE_DONT_SHARE_IT_WITH_ANYONE" # Your HF_TOKEN follow the README instructions

LOG_FILE = os.path.join(OUTPUT_PATH, "transcribed_files.txt")

# Load models
print("Loading diarization model...")
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=HF_TOKEN)
print("Loading Whisper model...")
whisper_model = whisper.load_model("medium")  # Change model size if needed

def load_transcribed():
    if not os.path.exists(LOG_FILE):
        return set()
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f.readlines())

def save_transcribed(file_name):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(file_name + "\n")

def transcribe_with_speakers(audio_file):
    audio = AudioSegment.from_file(audio_file)
    chunk_length_ms = 30 * 1000  # 30 seconds
    chunks = make_chunks(audio, chunk_length_ms)
    
    transcript_lines = []

    for i, chunk in enumerate(chunks):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            chunk.export(tmp.name, format="wav")
            chunk_path = tmp.name
        
        # Run diarization on the chunk
        diarization = pipeline(chunk_path)

        for turn, _, speaker in diarization.itertracks(yield_label=True):
            start_ms = int(turn.start * 1000)
            end_ms = int(turn.end * 1000)
            segment = chunk[start_ms:end_ms]

            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp2:
                segment.export(tmp2.name, format="wav")
                segment_path = tmp2.name
            
            try:
                result = whisper_model.transcribe(segment_path, language="en")
                text = result["text"].strip()
                if text:
                    transcript_lines.append(f"[{speaker}]: {text}")
            except Exception as e:
                print(f"Failed to transcribe segment {turn.start}-{turn.end} in chunk {i}: {e}")
            finally:
                if os.path.exists(segment_path):
                    os.remove(segment_path)

        if os.path.exists(chunk_path):
            os.remove(chunk_path)

    return "\n".join(transcript_lines)

if __name__ == "__main__":
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    transcribed = load_transcribed()

    for root, dirs, files in os.walk(RECORDER_PATH):
        for file_name in files:
            # Skip macOS hidden files
            if file_name.startswith("._"):
                continue
            if not file_name.lower().endswith((".mp3", ".wav")):
                continue
            if file_name in transcribed:
                print(f"Skipping already transcribed: {file_name}")
                continue

            full_path = os.path.join(root, file_name)
            print(f"Transcribing: {file_name}")
            transcript = transcribe_with_speakers(full_path)

            out_file = os.path.join(OUTPUT_PATH, os.path.splitext(file_name)[0] + ".txt")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(transcript)

            save_transcribed(file_name)
            print(f"Saved transcript: {out_file}")

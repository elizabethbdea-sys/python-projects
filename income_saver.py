import whisper
import sys
import os
from datetime import datetime

def transcribe_video(video_path):
    if not os.path.exists(video_path):
        print(f"❌ File not found: {video_path}")
        sys.exit(1)

    print(f"📂 Loading file: {video_path}")
    print("⏳ Loading Whisper model (first run downloads ~140MB)...")
    sys.stdout.flush()
    
    try:
        model = whisper.load_model("base")
        print("✅ Model loaded!")
        sys.stdout.flush()
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        sys.exit(1)

    print("🎙️  Transcribing... (may take several minutes for large files)")
    sys.stdout.flush()
    
    try:
        result = model.transcribe(video_path, verbose=True)
    except Exception as e:
        print(f"❌ Error transcribing: {e}")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{base_name}_transcript_{timestamp}.txt"
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"TRANSCRIPT: {base_name}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            f.write(result["text"])
        print(f"\n✅ Done! Transcript saved to: {output_file}")
        print(f"📄 Total characters: {len(result['text'])}")
    except Exception as e:
        print(f"❌ Error saving: {e}")
        print(result["text"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 transcribe.py <path_to_video>")
        sys.exit(1)
    
    print(f"Starting: {sys.argv[1]}")
    sys.stdout.flush()
    transcribe_video(sys.argv[1])
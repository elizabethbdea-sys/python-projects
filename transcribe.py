import whisper
import sys
import os
from datetime import datetime

def transcribe_video(video_path):
    # Check file exists
    if not os.path.exists(video_path):
        print(f"❌ File not found: {video_path}")
        sys.exit(1)

    print(f"📂 Loading file: {video_path}")
    print("⏳ Loading Whisper model (first run downloads it, ~140MB)...")
    
    # Load model - 'base' is fast and accurate enough for courses
    model = whisper.load_model("base")
    
    print("🎙️  Transcribing... (this may take a few minutes)")
    result = model.transcribe(video_path, verbose=False)
    
    # Create output filename based on input + timestamp
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{base_name}_transcript_{timestamp}.txt"
    
    # Save transcript
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"TRANSCRIPT: {base_name}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(result["text"])
    
    print(f"\n✅ Done! Transcript saved to: {output_file}")
    print(f"📄 Total characters: {len(result['text'])}")
    
    return output_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <path_to_video>")
        print("Example: python transcribe.py databricks_course.mp4")
        sys.exit(1)
    
    video_path = sys.argv[1]
    transcribe_video(video_path)
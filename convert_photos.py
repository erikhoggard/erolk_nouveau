import os
import subprocess
import sys

TARGET_DIR = "static/photos"

DELETE_ORIGINALS = False

# JPEG quality (1-5 is high quality, 1 is best)
JPEG_QUALITY = "1"
# -------------------

def run_command(command):
    """Runs an FFmpeg command and returns True on success, False on failure."""
    try:
        subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            shell=sys.platform == 'win32'
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ERROR: FFmpeg failed for {command[2]}")
        print(f"  FFmpeg output:\n{e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: 'ffmpeg' command not found. Is FFmpeg installed and in your system's PATH?")
        sys.exit(1)

if __name__ == "__main__":
    if not os.path.isdir(TARGET_DIR):
        print(f"Error: Target directory '{TARGET_DIR}' not found.")
        sys.exit(1)

    print(f"Searching for TIFF files in '{TARGET_DIR}'...")
    converted_count = 0

    for filename in os.listdir(TARGET_DIR):
        if filename.lower().endswith(('.tif', '.tiff')):
            input_path = os.path.join(TARGET_DIR, filename)

            # Create the new filename with a .jpg extension
            base_name = os.path.splitext(filename)[0]
            output_filename = f"{base_name}.jpg"
            output_path = os.path.join(TARGET_DIR, output_filename)

            print(f"Converting '{filename}'...")

            ffmpeg_command = [
                "ffmpeg",
                "-i", input_path,
                "-q:v", JPEG_QUALITY,
                "-pix_fmt", "yuvj420p",
                output_path
            ]

            if run_command(ffmpeg_command):
                converted_count += 1
                if DELETE_ORIGINALS:
                    try:
                        os.remove(input_path)
                        print(f"  -> Successfully converted and deleted '{filename}'.")
                    except OSError as e:
                        print(f"  -> ERROR: Could not delete original file: {e}")
                else:
                    print(f"  -> Successfully converted to '{output_filename}'.")

    print(f"\nConversion complete. Converted {converted_count} files.")
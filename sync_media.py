import subprocess
import sys
import os

PHOTO_BUCKET = "erolk-site-photos"
AUDIO_BUCKET = "erolk-site-audio"

PHOTO_DIR = "static/photos"
AUDIO_DIR = "static/audio"

def run_command(command):
    """Runs a command and checks for errors."""
    try:
        print(f"Executing: {' '.join(command)}")
        subprocess.run(command, check=True, shell=sys.platform == 'win32')
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except FileNotFoundError:
        print("Error: 'aws' command not found. Is the AWS CLI installed and in your PATH?")
        sys.exit(1)

def ensure_dir_exists(directory):
    """Creates a directory if it does not already exist."""
    if not os.path.exists(directory):
        print(f"Local directory '{directory}' not found. Creating it.")
        os.makedirs(directory)

if __name__ == "__main__":
    print("--- Starting Smart Sync ---")

    # Ensure local directories exist before syncing
    ensure_dir_exists(PHOTO_DIR)
    ensure_dir_exists(AUDIO_DIR)

    print("\nStep 1: Syncing Photos...")
    photo_pull_command = ["aws", "s3", "sync", f"s3://{PHOTO_BUCKET}", PHOTO_DIR]
    run_command(photo_pull_command)
    photo_push_command = ["aws", "s3", "sync", PHOTO_DIR, f"s3://{PHOTO_BUCKET}"]
    run_command(photo_push_command)

    print("\nStep 2: Syncing Audio...")
    audio_pull_command = ["aws", "s3", "sync", f"s3://{AUDIO_BUCKET}", AUDIO_DIR]
    run_command(audio_pull_command)
    audio_push_command = ["aws", "s3", "sync", AUDIO_DIR, f"s3://{AUDIO_BUCKET}"]
    run_command(audio_push_command)

    print("\n--- Smart Sync Complete ---")
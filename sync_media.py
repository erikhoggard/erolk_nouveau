import subprocess
import sys
import os

PHOTO_BUCKET = "erolk-site-photos"
AUDIO_BUCKET = "erolk-site-audio"

PHOTO_DIR = "assets/photos"
AUDIO_DIR = "assets/audio"

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

def standardize_image_extensions(directory):
    """Renames image files with uppercase extensions to lowercase."""
    print(f"\nStandardizing image extensions in '{directory}'...")
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg')) and not filename.endswith(('.jpg', '.jpeg')):
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, os.path.splitext(filename)[0] + os.path.splitext(filename)[1].lower())
                print(f"Renaming: {old_path} -> {new_path}")
                os.rename(old_path, new_path)


if __name__ == "__main__":
    print("--- Starting Smart Sync ---")

    # Ensure local directories exist before syncing
    ensure_dir_exists(PHOTO_DIR)
    ensure_dir_exists(AUDIO_DIR)

    print("\nStep 1: Syncing Photos...")
    # Pull remote changes first
    photo_pull_command = ["aws", "s3", "sync", f"s3://{PHOTO_BUCKET}", PHOTO_DIR]
    run_command(photo_pull_command)

    # Standardize extensions of local files (both new and pulled)
    standardize_image_extensions(PHOTO_DIR)

    # Push all changes back, ensuring consistent naming
    photo_push_command = ["aws", "s3", "sync", PHOTO_DIR, f"s3://{PHOTO_BUCKET}"]
    run_command(photo_push_command)


    print("\nStep 2: Syncing Audio...")
    audio_pull_command = ["aws", "s3", "sync", f"s3://{AUDIO_BUCKET}", AUDIO_DIR]
    run_command(audio_pull_command)
    audio_push_command = ["aws", "s3", "sync", AUDIO_DIR, f"s3://{AUDIO_BUCKET}"]
    run_command(audio_push_command)

    print("\n--- Smart Sync Complete ---")
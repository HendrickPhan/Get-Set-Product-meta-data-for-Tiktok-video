import json
import sys
from exiftool import ExifTool

def add_metadata(input_video, metadata):
    """
    Add metadata to a video file using exiftool.

    :param input_video: Path to the input video file.
    :param metadata: Dictionary containing metadata to add.
    """
    try:
        with ExifTool() as et:
            et.execute(*[f"-{key}={value}" for key, value in metadata.items()] + [input_video])
        print(f"Metadata successfully added to {input_video}")
    except Exception as e:
        print(f"Failed to add metadata: {e}")

def load_metadata(json_file):
    """
    Load metadata from a JSON file.

    :param json_file: Path to the JSON file.
    :return: Metadata dictionary.
    """
    try:
        with open(json_file, 'r') as f:
            metadata = json.load(f)
        return metadata
    except Exception as e:
        print(f"Failed to load metadata from {json_file}: {e}")
        sys.exit(1)

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python set_data.py <video_file> <metadata_json>")
        sys.exit(1)

    video_file = sys.argv[1]
    metadata_file = sys.argv[2]

    # Load metadata from JSON file
    metadata = load_metadata(metadata_file)

    # Add metadata to the video file
    add_metadata(video_file, metadata)

if __name__ == "__main__":
    main()

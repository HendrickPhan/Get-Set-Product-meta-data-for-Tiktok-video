import subprocess
import json
import sys

def get_metadata(file_path):
    """
    Extract metadata from a file using exiftool.

    :param file_path: Path to the file to analyze.
    :return: A dictionary containing the metadata.
    """
    try:
        # Run exiftool command
        result = subprocess.run(
            ['exiftool', '-json', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check for errors
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return None

        # Parse the JSON output
        metadata = json.loads(result.stdout)
        return metadata[0] if metadata else None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_metadata(metadata, output_file):
    """
    Save metadata to a JSON file.

    :param metadata: The metadata dictionary to save.
    :param output_file: Path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(metadata, f, indent=4)
        print(f"Metadata saved to {output_file}")
    except Exception as e:
        print(f"Failed to save metadata: {e}")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python get_data.py <filename> <output_json>")
        sys.exit(1)

    file_path = sys.argv[1]  # Input file
    output_file = sys.argv[2]  # Output JSON file

    # Extract metadata
    metadata = get_metadata(file_path)
    if metadata:
        print("Metadata extracted successfully:")
        # Extract Artwork
        for key, value in metadata.items():
            print(f"{key}: {value}")
        
        # Save metadata to a JSON file
        save_metadata({"artwork": metadata["Artwork"]}, output_file)
    else:
        print("Failed to extract metadata.")

if __name__ == "__main__":
    main()

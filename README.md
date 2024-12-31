# Metadata Management Tools

This repository contains two Python scripts, `set_data.py` and `get_data.py`, for managing metadata in video files using `exiftool`.

## Prerequisites

### 1. Install `ExifTool`

`ExifTool` is required to add or extract metadata. Install it using your system's package manager or download it from [ExifTool's official website](https://exiftool.org/).

#### Installation Examples:

- **macOS**: `brew install exiftool`
- **Ubuntu/Debian**: `sudo apt-get install libimage-exiftool-perl`
- **Windows**: Download and install from [ExifTool Windows](https://exiftool.org/).

### 2. Install Python Requirements

The `set_data.py` script uses the `exiftool` Python library. Install it using `pip`:

```bash
pip install pyexiftool
```

## Scripts Overview

### 1. `set_data.py`

Adds custom metadata to a video file based on a JSON input.

#### Usage

```bash
python set_data.py <video_file> <metadata_json>
```

#### Parameters

- `<video_file>`: The path to the video file where metadata should be added.
- `<metadata_json>`: The path to the JSON file containing metadata to be added.

#### Example

```bash
python set_data.py video.mov data.json
```

##### Example Metadata JSON (`data.json`)

```bash
{     
	"artwork": "{\"source_type\": \"vicut\", \"data\": {\"appVersion\": \"13.4.1\", \"region\": \"VN\"}}"
}
```
#### Output

- The script modifies the video file in-place, adding the specified metadata.
- Success and error messages are displayed in the terminal.

---

### 2. `get_data.py`

Extracts metadata from a video file and saves it to a JSON file.

#### Usage
```bash
python get_data.py <video_file> <output_json>
```

#### Parameters

- `<video_file>`: The path to the video file from which metadata should be extracted.
- `<output_json>`: The path to the JSON file where extracted metadata will be saved.

#### Example
```bash
python get_data.py video.mov metadata.json
```

#### Output

- Metadata is saved in the specified JSON file.
- Success and error messages are displayed in the terminal.

---

## Examples

### Adding Metadata

```bash
python set_data.py my_video.mov metadata.json
```

### Extracting Metadata
```bash
python get_data.py my_video.mov extracted_metadata.json
```

---

## Troubleshooting

1. **Error: `exiftool` not found**
    
    - Ensure `ExifTool` is installed and accessible in your system's PATH.
2. **Error: Failed to load metadata**
    
    - Verify that the JSON file provided as input to `set_data.py` is correctly formatted.
3. **Error: Permission denied**
    
    - Ensure you have write permissions for the video file.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

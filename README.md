# M3U Playlist Filter and Processor

## Overview
A versatile Python script for filtering and processing M3U playlist files with flexible filtering options.

## Features
- `Filter M3U playlists by group titles`
- Preserve original file structure
- Support for multiple filter keywords
- Automatic 4K/UHD channel inclusion
- Default full file copy when no filters specified

## Usage

### Basic Syntax
```bash
python3 script_name.py input.m3u output.m3u [filter1] [filter2] ...
```

### Examples
```bash
# Copy entire playlist
python3 script.py input.m3u output.m3u

# Filter specific channels
python3 script.py input.m3u output.m3u UK DE
```

## Filtering Rules
- Channels with group titles matching specified filters are included
- 4K/UHD channels are always included
- When no filters are provided, the entire playlist is copied

## Requirements
- Python 3.x
- No additional libraries required

## License
MIT License

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss proposed modifications.


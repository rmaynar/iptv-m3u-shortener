import re
import sys

def process_m3u_file(input_file, output_file, filters):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Write the #EXTM3U line first
        outfile.write('#EXTM3U\n')
        include_next_line = False

        for line in infile:
            line = line.strip()
            if line.startswith('#EXTM3U'):
                continue  # Skip as it's already written
            elif line.startswith('#EXTINF'):
                if not filters:  # If no filters are provided, copy all lines
                    outfile.write(line + '\n')
                    include_next_line = True
                else:
                    # Match group-title and tvg-name fields
                    group_title_match = re.search(r'group-title="([^"]*)"', line)
                    tvg_name_match = re.search(r'tvg-name="([^"]*)"', line)
                    
                    group_title = group_title_match.group(1) if group_title_match else ""
                    tvg_name = tvg_name_match.group(1) if tvg_name_match else ""

                    # Check if group-title starts with filter + '|' or tvg-name starts with filter
                    if (any(group_title.startswith(filter_word + '|') for filter_word in filters) or 
                        any(tvg_name.startswith(filter_word) for filter_word in filters) or 
                        group_title == "4K| UHD 3840P"):
                            outfile.write(line + '\n')
                            include_next_line = True
                    else:
                        include_next_line = False
            elif include_next_line or not filters:
                outfile.write(line + '\n')
                include_next_line = False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script_name.py input_file output_file [filter1 filter2 ...]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    filters = sys.argv[3:]  # Remaining arguments are treated as filters

    process_m3u_file(input_file, output_file, filters)

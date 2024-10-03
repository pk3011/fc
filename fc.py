import requests
import json

# URL of the JSON data
url = "https://raw.githubusercontent.com/drmlive/fancode-live-events/refs/heads/main/fancode.json"

# Fetch JSON data
response = requests.get(url)
data = response.json()

# M3U header
m3u_content = "#EXTM3U\n"

# Process each item in the JSON data
for item in data.get("data", []):
    tournament = item.get("tournament", "Unknown Tournament")
    poster = item.get("poster", "")
    initial_url = item.get("initialUrl", "")
    
    # Add entry to M3U content
    m3u_content += f'#EXTINF:-1 group-title="fancode" tvg-logo="{poster}",{tournament}\n'
    m3u_content += f'{initial_url}\n'

# Save M3U content to a file
with open("fc.m3u", "w") as m3u_file:
    m3u_file.write(m3u_content)

print("M3U playlist saved as fc.m3u")

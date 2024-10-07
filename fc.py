import requests
import json

# Define the URL of the JSON data
url = 'https://raw.githubusercontent.com/drmlive/fancode-live-events/refs/heads/main/fancode.json'

# Fetch the JSON data from the URL
response = requests.get(url)
data = response.json()

# Create a function to generate the M3U playlist
def create_m3u_playlist(json_data):
    playlist = "#EXTM3U\n"
    
    # Loop through each match in the JSON data
    for match in json_data['matches']:
        title = match['title']
        logo = match['src']
        stream_url = match['adfree_url']
        
        # Add the channel details in M3U format
        playlist += f'#EXTINF:-1 tvg-logo="{logo}" group-title="fancode", {title}\n{stream_url}\n'
    
    return playlist

# Generate the M3U playlist
m3u_playlist = create_m3u_playlist(data)

# Save the M3U playlist to a file
with open('fc.m3u', 'w') as f:
    f.write(m3u_playlist)

print("M3U playlist created successfully!")

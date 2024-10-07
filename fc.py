import requests
import json

# URL to fetch the JSON data
url = "https://raw.githubusercontent.com/drmlive/fancode-live-events/refs/heads/main/fancode.json"

# Function to create M3U playlist
def create_m3u_playlist(json_url):
    response = requests.get(json_url)
    
    if response.status_code == 200:
        data = response.json()

        # Check if 'matches' exist in the JSON data
        if 'matches' not in data:
            print("No matches data found!")
            return

        matches = data['matches']

        # Open the M3U file to write the playlist
        with open("fc.m3u", "w") as m3u_file:
            # Writing M3U header
            m3u_file.write("#EXTM3U\n")
            
            # Iterate through each match in the matches list
            for match in matches:
                try:
                    # Extract relevant details for the playlist
                    title = match['title']
                    logo = match['src']
                    stream_url = match['adfree_url']  # Fixing the KeyError
                    
                    # Write the M3U details
                    m3u_file.write(f'#EXTINF:-1 group-title="fancode" tvg-logo="{logo}",{title}\n')
                    m3u_file.write(f'{stream_url}\n')
                except KeyError as e:
                    print(f"KeyError: {e} in match: {match.get('title', 'Unknown')}")
    else:
        print("Failed to fetch the JSON data. Status code:", response.status_code)

# Call the function to create the playlist
create_m3u_playlist(url)


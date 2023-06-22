import requests

# SnapXCDN link
snapxcdn_link = "https://snapxcdn.com/v2/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJodHRwczovL3Njb250ZW50LmNkbmluc3RhZ3JhbS5jb20vdi90NjYuMzAxMDAtMTYvNDQ4MDQyMjJfMTQ1ODc1NTYxODIwMTAwXzI1NzU2NjEyOTQ3ODcyMjY4NzBfbi5tcDQ_X25jX2h0PXNjb250ZW50LmNkbmluc3RhZ3JhbS5jb20mX25jX2NhdD0xMDgmX25jX29oYz1aTmZId3VrVTV3Z0FYODhfR1A5JmVkbT1BUHMxN0NVQkFBQUEmY2NiPTctNSZvaD0wMF9BZkNlRVBsU2NUSUZZNXBoQWVXZ2ZULWdpazhxX2tiZFBZR2lneXJCaUxnamJRJm9lPTY0ODNBNTI4Jl9uY19zaWQ9ZGYwNDRmIiwiZmlsZW5hbWUiOiJTbmFwaW5zdGEuYXBwX3ZpZGVvXzQ0ODA0MjIyXzE0NTg3NTU2MTgyMDEwMF8yNTc1NjYxMjk0Nzg3MjI2ODcwX24ubXA0In0.PHt-rMXa1ohd1B1nJN7L4rReNHQsOR8P09nMAnWQYFM&dl=1&dl=1"

# Send a GET request to the SnapXCDN link
response = requests.get(snapxcdn_link)

# Check if the request was successful
if response.status_code == 200:
    # Save the video file
    with open("downloaded_video.mp4", "wb") as video_file:
        video_file.write(response.content)
    print("Video downloaded successfully!")
else:
    print("Failed to download the video.")

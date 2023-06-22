import os
import openai
from instabot import Bot

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Instagram credentials
username = "<your_username>"
password = "<your_password>"

# Path to the reels directory
reels_directory = "<path_to_reels_directory>"

# Generate caption using ChatGPT
def generate_caption(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Initialize the bot and log in
bot = Bot()
bot.login(username=username, password=password)

# Get the list of reels
reels = os.listdir(reels_directory)

# Loop through each reel and post to Instagram with generated captions
for reel in reels:
    reel_path = os.path.join(reels_directory, reel)

    # Generate a caption for the reel
    prompt = "Generate a creative Instagram caption for a video reel:"
    caption = generate_caption(prompt)

    # Upload the reel with the generated caption
    bot.upload_video(reel_path, caption=caption)

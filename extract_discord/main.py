import asyncio
import os
from discord_bot import run_discord_bot

# Ensure to replace 'YOUR_TOKEN' and 'CHANNEL_ID' with your actual Discord bot token and channel ID
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', 'YOUR_TOKEN')  # Replace 'YOUR_TOKEN' with your bot's token
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 'YOUR_CHANNEL_ID'))  # Replace 'YOUR_CHANNEL_ID' with your channel ID

if __name__ == "__main__":
    run_discord_bot(DISCORD_TOKEN, CHANNEL_ID)

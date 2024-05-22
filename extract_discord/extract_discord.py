!pip install discord.py
!pip install pandas
!pip install openpyxl

import discord
import asyncio
import pandas as pd

# Intents
intents = discord.Intents.default()
intents.messages = True  # Allow message related events

# Initialize the Discord client with intents
client = discord.Client(intents=intents)

# Create an empty DataFrame
df = pd.DataFrame(columns=['Author', 'Content'])

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Replace CHANNEL_ID with the ID of your #general channel
    channel = client.get_channel(CHANNEL_ID)

    # Fetch message history
    messages = []
    async for message in channel.history(limit=10):  # Fetch the last 10 messages
        messages.append((message.author.name, message.content))

    # Update DataFrame
    global df  # Use the global DataFrame
    df = pd.DataFrame(messages, columns=['Author', 'Content'])

    # Print DataFrame
    print(df)

# Replace 'YOUR_TOKEN' with your bot's token
async def main():
    await client.start('YOUR_TOKEN')

# Replace 'YOUR_TOKEN' with your bot's token
# Start the bot using asyncio.create_task()
loop = asyncio.get_event_loop()
loop.create_task(main())

# Export DataFrame to Excel
df.to_excel('message_history.xlsx', index=False)

import discord
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
    await fetch_messages(CHANNEL_ID)

async def fetch_messages(channel_id):
    channel = client.get_channel(channel_id)
    if channel is None:
        print(f"Channel with ID {channel_id} not found")
        return

    # Fetch message history
    messages = []
    async for message in channel.history(limit=10):  # Fetch the last 10 messages
        messages.append((message.author.name, message.content))

    # Update DataFrame
    global df  # Use the global DataFrame
    df = pd.DataFrame(messages, columns=['Author', 'Content'])

    # Print DataFrame
    print(df)

    # Save DataFrame to Excel
    df.to_excel('message_history.xlsx', index=False)
    print("Messages saved to message_history.xlsx")

def run_discord_bot(token, channel_id):
    global CHANNEL_ID
    CHANNEL_ID = channel_id
    client.run(token)

import discord
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
print(BOT_TOKEN)
intents = discord.Intents.default()
intents.members = True
# intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print("Message author = ",message.author)
    print("Client user = ",client.user)
    if message.author == client.user:
        return
    print()
    print(message)
    print()
    # if message.author == client.user:
    #     return
    print(message.content)
    if message.content.startswith('/hello'):
        
        await message.channel.send(f'Hello {message.author.mention}, thanks for your message!')
        print("Done")
    
    # if message.content.startswith('/gen'):
    #     with open("result.png", "rb") as f:
    #         await message.channel.send(file=discord.File(f))

client.run(BOT_TOKEN)
#Import necessary libraries and modules
import discord
from class_chatgpt import Gpt_API
from discord.ext import commands


#Loading .env file and it's information
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')

# Setting up discord bot client
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

# Welcome message
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Message sending function
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Send the reply to the user
    elif isinstance(message.channel, discord.channel.DMChannel):
        print(message.content)
        if message.content.startswith("/ask"):
            query = message.content[5:]
            res_obj = Gpt_API(query)
            result = res_obj.get_result()
            # If the message was sent in a private message, reply in a private message
            await message.reply(f"{result}",mention_author=True)
        else:
            return
    # If the bot is asked in a server text channel
    else:
        # if message start with '?' , the reply will be directed to private message
        print(message.content)
        if message.content.startswith("?"):
            if message.content.startswith("?ask"):
                query = message.content[5:]
                res_obj = Gpt_API(query)
                result = res_obj.get_result()
                server = message.guild
                server_mention = f'{server.name}'
                embed = discord.Embed(title=f"From {server_mention} >>\nMessage == {message.content}\n\n", description=f"{result}", color=discord.Color.blue())
                await message.author.send(embed=embed)
            else:
                return
        else:
            if message.content.startswith("/ask"):
                query = message.content[5:]
                res_obj = Gpt_API(query)
                result = res_obj.get_result()
                # If the message was sent in a server text channel, reply in the same channel
                await message.reply(f"{result}")
            else:
                return

# Run the bot
bot.run(BOT_TOKEN)

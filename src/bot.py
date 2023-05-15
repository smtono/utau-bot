"""

"""

import os

import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Discord Setup
intents = discord.Intents().default()
client = commands.Bot(command_prefix="utau ", intents=intents)

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "ping", description = "Simple response to check if the bot is online")
async def ping(interaction):
    await interaction.response.send_message("At your service!")

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

stop = False
# Conversation
@client.event
async def on_message(message: discord.Message):
    global stop

client.run(TOKEN)

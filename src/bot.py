"""
utau bot used for making music
"""

import os

import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

import input_parser

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
    
@tree.command(name = "compose", description = "Make music like a pleb")
async def compose(interaction: discord.Interaction, *, notes: str):
    await interaction.response.defer()
    input_parser.parse(notes)
    await interaction.followup.send(file=discord.File(os.path.join(os.getcwd(), "output", "output.mp3"))) # pylint: disable=syntax-error

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(TOKEN)

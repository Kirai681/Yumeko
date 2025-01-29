import discord
from discord.ext import commands

from dotenv import load_dotenv

import os

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
if DISCORD_TOKEN is None:
    raise ValueError("TOKEN is not set.")

PREFIX = "?"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.run(DISCORD_TOKEN)

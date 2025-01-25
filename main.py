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


async def load_cogs(bot: commands.Bot, path: str = "cogs") -> None:
    for directory, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".py") and not filename.startswith("_"):
                module_path = os.path.join(directory, filename).replace(os.sep, ".")
                cog_path = module_path.removesuffix(".py")
                try:
                    await bot.load_extension(cog_path)
                    print(f"Loaded '{cog_path}' sucessfully.")
                except Exception as e:
                    print(f"Error while loading cog '{cog_path}': {e}")


async def custom_setup_hook() -> None:
    await load_cogs(bot)


bot.setup_hook = custom_setup_hook


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}.")


bot.run(DISCORD_TOKEN)

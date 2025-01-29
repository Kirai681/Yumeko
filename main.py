import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
if DISCORD_TOKEN is None:
    raise ValueError("TOKEN is not set.")

PREFIX = "?"
INTENTS = discord.Intents.all()

bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)


async def load_extensions(bot: commands.Bot, path: str = "extensions") -> None:
    """Load extensions from the specified directory.

    :param bot: The bot instance to load extensions for.
    :type bot: commands.Bot
    :param path: The path to the directory where extensions are located,
        defaults to "extensions"
    :type path: str, optional
    :return: None
    """
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            if not filename.startswith("_") and filename.endswith(".py"):
                extension = os.path.join(root, filename).removesuffix(".py")
                try:
                    await bot.load_extension(extension.replace(os.sep, "."))
                    print(f"Loaded extension {extension}.")
                except Exception as e:
                    print(f"Extension {extension} couldn't be loaded: {e}")


async def custom_setup_hook() -> None:
    """Custom setup hook for the bot to load extensions before logging in.

    :return: None
    """
    await load_extensions(bot)


bot.setup_hook = custom_setup_hook

bot.run(DISCORD_TOKEN)

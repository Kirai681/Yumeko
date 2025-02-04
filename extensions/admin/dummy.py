from discord.ext import commands


class Dummy(commands.Cog):
    """Dummy cog for testing purposes"""

    def __init__(self, bot: commands.Bot) -> None:
        """Initalizes the Dummy cog.

        :param bot: The instance of the bot using this cog.
        :type bot: commands.Bot
        """
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    """Sets up the Dummy cog by adding it to the bot.

    :param bot: The bot instance to which the cog is added to.
    :type bot: commands.Bot
    """
    await bot.add_cog(Dummy(bot))

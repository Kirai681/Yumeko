from discord.ext import commands

from typing import Optional


class Sync(commands.Cog):
    """
    Handles administrative command for syncing app_commands.

    :ivar bot: The instance of the bot using this cog.
    :vartype bot: commands.Bot
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initalizes the Sync cog.

        :param bot: The instance of the bot using this cog.
        :type bot: commands.Bot
        """
        self.bot = bot

    @commands.command(name="sync", help="...")
    async def sync(
        self,
        ctx: commands.Context,
        operation: Optional[str] = None,
    ) -> None: ...


async def setup(bot: commands.Bot) -> None:
    """Sets up the Sync cog by adding it to the bot.

    :param bot: The bot instance to which the cog is added to.
    :type bot: commands.Bot
    """
    await bot.add_cog(Sync(bot))

from discord.ext import commands

from utils import EmbedHelper


class Loader(commands.Cog):
    """
    Handles administrative commands for (re/un)loading bot extensions.

    :ivar bot: The instance of the bot using this cog.
    :vartype bot: commands.Bot
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initalizes the Loader cog.

        :param bot: The instance of the bot using this cog.
        :type bot: commands.Bot
        """
        self.bot = bot

    @commands.command(name="reload", help="Reloads a specific extension.")
    async def reload(self, ctx: commands.Context, extension: str) -> None:
        extension_path = f"extensions.{extension}"
        try:
            await self.bot.reload_extension(extension_path)
            embed = EmbedHelper.success_embed(
                title="Reloaded Successfully",
                description=f"Extension {extension} was reloaded successfully",
            )
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            # TODO: Implement proper specific error handling
            ...


async def setup(bot: commands.Bot) -> None:
    """Sets up the admin cog by adding it to the bot.

    :param bot: The bot instance to which the cog is added to.
    :type bot: commands.Bot
    """
    await bot.add_cog(Loader(bot))

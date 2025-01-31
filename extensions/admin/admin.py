from discord.ext import commands

from utils import EmbedHelper


class Admin(commands.Cog):
    """
    Handles administrative commands for the bot.

    :ivar bot: The instance of the bot using this cog.
    :vartype boy: commands.Bot
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initalizes the admin cog.

        :param bot: The instance of the bot using this cog.
        :type bot: commands.Bot
        :return: None
        :rtype: None
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
    :return: None
    :rtype: None
    """
    await bot.add_cog(Admin(bot))

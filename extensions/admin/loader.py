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

    @commands.command(name="load", help="Loads a specific extension.")
    async def load(self, ctx: commands.Context, extension: str) -> None:
        """Loads a specific extension.

        :param ctx: The context in which the command was invoked.
        :type ctx: commands.Context
        :param extension: The extension to reload.
        :type extension: str
        """
        extension_path = f"extensions.{extension}"

    @commands.command(name="reload", help="Reloads a specific extension.")
    async def reload(self, ctx: commands.Context, extension: str) -> None:
        """Reloads a specific extension.

        :param ctx: The context in which the command was invoked.
        :type ctx: commands.Context
        :param extension: The extension to reload.
        :type extension: str
        """
        extension_path = f"extensions.{extension}"
        try:
            if extension_path not in self.bot.extensions:
                raise commands.ExtensionNotFound(extension_path)

            await self.bot.reload_extension(extension_path)
            embed = EmbedHelper.success_embed(
                title="Reloaded Successfully",
                description=f"Extension `{extension}` was reloaded successfully",
            )
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            embed = EmbedHelper.error_embed(
                title="Extension Not Found",
                description=f"Extension `{extension}` does not exist.",
            )
            await ctx.send(embed=embed)
        except commands.ExtensionNotLoaded:
            embed = EmbedHelper.error_embed(
                title="Extension Not Loaded",
                description=f"Cannot reload extension `{extension}` because it is not loaded.",
            )
            await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """Sets up the admin cog by adding it to the bot.

    :param bot: The bot instance to which the cog is added to.
    :type bot: commands.Bot
    """
    await bot.add_cog(Loader(bot))

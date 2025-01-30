import discord
from discord import app_commands
from discord.ext import commands

from utils import EmbedHelper


class ErrorHandler(commands.Cog):
    """
    Global error handler for prefix and app commands.

    :ivar bot: The instance of the bot using this cog.
    :vartype boy: commands.Bot
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initalizes the error handler cog.

        :param bot: The instance of the bot using this cog.
        :type bot: commands.Bot
        :return: None
        :rtype: None
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(
        self,
        ctx: commands.Context,
        error: commands.CommandError,
    ) -> None:
        """Listener for errors in prefix commands.

        :param ctx: The command context where the error occured.
        :type ctx: commands.Context
        :param error: The error raised during command execution.
        :type error: commands.CommandError
        :return: None
        :rtype: None
        """
        if isinstance(error, commands.CommandNotFound):
            embed = EmbedHelper.error_embed(
                "Command Not Found",
                f"Use `{ctx.prefix}help` to see available commands.",
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = EmbedHelper.error_embed(
                "Missing Argument",
                f"Required argument is missing: `<{error.param.name}>`",
            )
            await ctx.send(embed=embed)
        else:
            embed = EmbedHelper.error_embed(
                "Unexpected Error",
                f"{error}",
            )
            await ctx.send(embed=embed)

    # TODO: Implement error interface for app_commands
    @commands.Cog.listener()
    async def on_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.AppCommandError,
    ) -> None: ...


async def setup(bot: commands.Bot) -> None:
    """Sets up the error handler cog by adding it to the bot.

    :param bot: The bot instance to which the cog is added to.
    :type bot: commands.Bot
    :return: None
    :rtype: None
    """
    await bot.add_cog(ErrorHandler(bot))

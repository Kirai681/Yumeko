import discord
from discord import app_commands
from discord.ext import commands

from typing import Union


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

    async def send_error_feedback(
        self,
        destination: Union[commands.Context, discord.Interaction],
        title: str,
        description: str,
        ephermeral: bool = True,
    ) -> None:
        """Sends an error embed to a user in a command context or interaction.

        :param destination: The destination for the message.
        :type destination: Union[commands.Context, discord.Interaction]
        :param title: The title of the embed.
        :type title: str
        :param description: The description of the embed.
        :type description: str
        :param ephermeral: If True, send an ephermeral message,
            defaults to True
        :type ephermeral: bool, optional
        :return: None
        :rtype: None
        """
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Color.red(),
        )
        if isinstance(destination, commands.Context):
            await destination.send(embed=embed)
        elif isinstance(destination, discord.Interaction):
            await destination.response.send_message(
                embed=embed,
                ephemeral=ephermeral,
            )

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
            await self.send_error_feedback(
                ctx,
                "Command Not Found",
                f"Use `{ctx.prefix}help` to see available commands.",
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await self.send_error_feedback(
                ctx,
                "Missing Argument",
                f"Required argument is missing: `<{error.param.name}>`",
            )
        else:
            await self.send_error_feedback(
                ctx,
                "Unexpected Error",
                f"{error}",
            )

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

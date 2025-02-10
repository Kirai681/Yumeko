from discord.ext import commands

from utils import EmbedHelper

from typing import Optional
from typing import Literal


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

    @commands.command(
        name="sync",
        help="Syncs app_commands basded on the provided action.\n"
        "`*`: Sync globally\n"
        "`~`: Sync current guild\n"
        "`!`: Clear globally\n"
        "`?`: Clear current guild",
    )
    async def sync(
        self,
        ctx: commands.Context,
        action: Optional[Literal["*", "~", "!", "?"]] = commands.parameter(
            default=None,
            description="The action to execute.",
        ),
    ) -> None:
        match action:
            case _:
                embed = EmbedHelper.error_embed(
                    title="Invalid Action",
                    description=f"Use `{ctx.prefix}help {ctx.command}` to see available actions.",
                )
                await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """Sets up the Sync cog by adding it to the bot.

    :param bot: The bot instance to which the cog is added to.
    :type bot: commands.Bot
    """
    await bot.add_cog(Sync(bot))

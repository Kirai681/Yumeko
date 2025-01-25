from discord.ext import commands

from utils import EmbedHelper
from utils import EmbedType


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="reload")
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, extension: str) -> None: ...


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))

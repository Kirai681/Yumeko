from discord.ext import commands

from utils import EmbedHelper


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="reload")
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, extension: str) -> None: ...

    @commands.Cog.listener()
    async def on_command_error(
        self, ctx: commands.Context, error: commands.errors.CommandError
    ) -> None:
        if isinstance(error, commands.MissingRequiredArgument):
            embed = EmbedHelper.create_error_embed(
                f"Missing argument: {error.param.name}\n"
                f"Usage: `{ctx.prefix}{ctx.command} {ctx.command.signature}`",
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            embed = EmbedHelper.create_error_embed(
                "Command not found.\n"
                f"Use `{ctx.prefix}help` to see available commands.",
            )
            await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))

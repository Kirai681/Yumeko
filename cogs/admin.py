from discord.ext import commands

from utils import EmbedHelper


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="reload", description="Reloads a specific extension.")
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, extension: str) -> None:
        extension_path = f"cogs.{extension}"
        try:
            await self.bot.reload_extension(extension_path)
            embed = EmbedHelper.create_success_embed(
                f"Reloaded extension `{extension}`."
            )
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            embed = EmbedHelper.create_error_embed(
                f"Extension `{extension}` doesn't exist."
            )
            await ctx.send(embed=embed)

    @commands.command(name="unload", description="Unloads a specific extension.")
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, extension: str) -> None:
        extension_path = f"cogs.{extension}"
        try:
            await self.bot.unload_extension(extension_path)
            embed = EmbedHelper.create_success_embed(
                f"Unloaded extension `{extension}`."
            )
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            embed = EmbedHelper.create_error_embed(
                f"Extension `{extension}` doesn't exist."
            )
            await ctx.send(embed=embed)

    @commands.command(name="load", description="Loads a specific extension.")
    @commands.is_owner()
    async def load(self, ctx: commands.Context, extension: str) -> None:
        extension_path = f"cogs.{extension}"
        try:
            await self.bot.load_extension(extension_path)
            embed = EmbedHelper.create_success_embed(
                f"Loaded extension `{extension}`.",
            )
            await ctx.send(embed=embed)
        except commands.ExtensionNotFound:
            embed = EmbedHelper.create_error_embed(
                f"Extension `{extension}` doesn't exist."
            )
            await ctx.send(embed=embed)

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
        elif isinstance(error, commands.NotOwner):
            embed = EmbedHelper.create_error_embed(
                "You don't have the permission to run this command.",
            )
            await ctx.send(embed=embed)
        else:
            embed = EmbedHelper.create_error_embed("An unexpected error occured.")
            await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))

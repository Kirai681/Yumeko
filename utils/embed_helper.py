import discord
from discord import Embed
from utils import Icons

from enum import Enum


class Colors(Enum):
    SUCCESS = discord.Color.green()
    INFO = discord.Color.blue()
    ERROR = discord.Color.red()


class EmbedHelper:
    @staticmethod
    def create_success_embed(descrtiption: str) -> Embed:
        return Embed(
            title=f"{Icons.SUCCESS.value} Success",
            description=descrtiption,
            color=Colors.SUCCESS.value,
        )

    @staticmethod
    def create_error_embed(descrtiption: str) -> Embed:
        return Embed(
            title=f"{Icons.ERROR.value} Error",
            description=descrtiption,
            color=Colors.ERROR.value,
        )

    @staticmethod
    def create_info_embed(descrtiption: str) -> Embed:
        return Embed(
            title=f"{Icons.INFO.value} Information",
            description=descrtiption,
            color=Colors.INFO.value,
        )

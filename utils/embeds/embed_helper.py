import discord


class EmbedHelper:
    """A utility class to create standardized Discord embed messages.

    :cvar success_color: The color used for success embeds.
    :vartype success_color: discord.Color
    :cvar info_color: The color used for info embeds.
    :vartype info_color: discord.Color
    :cvar error_color: The color used for error embeds.
    :vartype error_color: discord.Color
    """

    success_color = discord.Color.green()
    info_color = discord.Color.blurple()
    error_color = discord.Color.red()

    def __new__(cls) -> None:
        """Prevents instantiation of the class.

        :raises TypeError: Always raised to prevent instantiation.
        """
        raise TypeError(f"{cls.__name__} cannot be instantiated.")

    @staticmethod
    def success_embed(title: str, description: str) -> discord.Embed:
        """Creates a success embed with a green color.

        :param title: The title of the embed.
        :type title: str
        :param description: The description of the embed.
        :type description: str
        :return: A Discord embed for success messages.
        :rtype: discord.Embed
        """
        return discord.Embed(
            title=title,
            description=description,
            color=EmbedHelper.success_color,
        )

    @staticmethod
    def info_embed(title: str, description: str) -> discord.Embed:
        """Creates an info embed with a blurple color.

        :param title: The title of the embed.
        :type title: str
        :param description: The description of the embed.
        :type description: str
        :return: A Discord embed for info messages.
        :rtype: discord.Embed
        """
        return discord.Embed(
            title=title,
            description=description,
            color=EmbedHelper.info_color,
        )

    @staticmethod
    def error_embed(title: str, description: str) -> discord.Embed:
        """Creates an error embed with a red color.

        :param title: The title of the embed.
        :type title: str
        :param description: The description of the embed.
        :type description: str
        :return: A Discord embed for error messages.
        :rtype: discord.Embed
        """
        return discord.Embed(
            title=title,
            description=description,
            color=EmbedHelper.error_color,
        )

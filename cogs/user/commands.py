import logging
import discord
from discord.ext import commands
from discord import app_commands

from services.user_service import UserService
from utils.embeds import user_embed, avatar_embed

logger = logging.getLogger(__name__)

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = UserService()
        logger.info("User Cog initialized")

    @app_commands.command(name="user", description="Get user info")
    @app_commands.describe(member="User to fetch info about")
    async def user(
        self,
        interaction: discord.Interaction,
        member: discord.Member = None
    ):
        member = member or interaction.user
        logger.info(f"Command /user invoked by {interaction.user} for {member}")

        try:
            data = self.service.get_user_data(member)
            embed = user_embed(data)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            logger.error(f"Error in /user command: {e}", exc_info=True)
            await interaction.response.send_message("An error occurred fetching user data.", ephemeral=True)
        
    @app_commands.command(name="avatar", description="Get user's avatar")
    @app_commands.describe(member="User to fetch avatar of")
    async def avatar(
        self,
        interaction: discord.Interaction,
        member: discord.Member = None
    ):
        member = member or interaction.user
        logger.info(f"Command /avatar invoked by {interaction.user} for {member}")

        try:
            data = self.service.get_avatar(member)
            embed = avatar_embed(data)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            logger.error(f"Error in /avatar command: {e}", exc_info=True)
            await interaction.response.send_message("An error occurred fetching the avatar.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(User(bot))

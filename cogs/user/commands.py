from discord.ext import commands
from discord import app_commands
import discord

from services.user_service import UserService
from utils.embeds import user_embed,avatar_embed

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = UserService()

    @app_commands.command(name="user", description="Get user info")
    @app_commands.describe(member="User to fetch info about")
    async def user(
        self,
        interaction: discord.Interaction,
        member: discord.Member = None
    ):
        member = member or interaction.user

        data = self.service.get_user_data(member)
        embed = user_embed(data)

        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="avatar", description="Get user's avatar")
    @app_commands.describe(member="User to fetch avatar of")
    async def avatar(
        self,
        interaction: discord.Interaction,
        member: discord.Member = None
    ):
        member = member or interaction.user

        data = self.service.get_avatar(member)
        embed = avatar_embed(data)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(User(bot))

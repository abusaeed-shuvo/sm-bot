import logging
import discord
from discord import app_commands
from discord.ext import commands
from database.db import SessionLocal
from services.snippet_service import (
    add_snippet, fetch_snippet, remove_snippet, fetch_all_snippets
)

logger = logging.getLogger(__name__)

class SnippetGroup(app_commands.Group, name="snippet"):
    """All snippet-related commands under the /snippet group"""

    @app_commands.command(name="add", description="Create a new snippet")
    async def add(self, interaction: discord.Interaction, name: str, content: str):
        async with SessionLocal() as db:
            try:
                snippet = await add_snippet(db, name, content, str(interaction.user.id))
                await interaction.response.send_message(f"✅ Snippet `{snippet.name}` created!", ephemeral=True)
            except Exception as e:
                logger.error(f"Failed to create snippet: {e}", exc_info=True)
                await interaction.response.send_message("❌ Failed to create snippet.", ephemeral=True)

    @app_commands.command(name="get", description="View a snippet")
    async def get(self, interaction: discord.Interaction, name: str):
        async with SessionLocal() as db:
            snippet = await fetch_snippet(db, name)
            if not snippet:
                return await interaction.response.send_message("❌ Not found", ephemeral=True)
            await interaction.response.send_message(f"```{snippet.content}```")

    @app_commands.command(name="remove", description="Delete a snippet")
    async def remove(self, interaction: discord.Interaction, name: str):
        async with SessionLocal() as db:
            success = await remove_snippet(db, name)
            if success:
                await interaction.response.send_message(f"✅ Deleted `{name}`", ephemeral=True)
            else:
                await interaction.response.send_message("❌ Snippet not found.", ephemeral=True)

    @app_commands.command(name="list", description="List all available snippets")
    async def list_snippets(self, interaction: discord.Interaction):
        async with SessionLocal() as db:
            snippets = await fetch_all_snippets(db)
            if not snippets:
                return await interaction.response.send_message("No snippets found", ephemeral=True)
            names = "\n".join([f"• {s.name}" for s in snippets])
            await interaction.response.send_message(f"**Available Snippets:**\n{names}")

class SnippetCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Register the group to the command tree
        self.bot.tree.add_command(SnippetGroup())

async def setup(bot):
    await bot.add_cog(SnippetCog(bot))

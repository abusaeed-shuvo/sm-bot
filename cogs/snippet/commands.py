import discord
from discord import app_commands
from discord.ext import commands

from database.db import SessionLocal
from services.snippet_service import (
    add_snippet,
    fetch_snippet,
    remove_snippet,
    fetch_all_snippets
)

class Snippet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="snippet_create", description="Create a snippet")
    async def create(self, interaction: discord.Interaction, name: str, content: str):
        db = SessionLocal()

        snippet = add_snippet(db, name, content, str(interaction.user.id))

        await interaction.response.send_message(
            f" Snippet `{snippet.name}` created!",
            ephemeral=True
        )

    @app_commands.command(name="snippet_get", description="Get a snippet")
    async def get(self, interaction: discord.Interaction, name: str):
        db = SessionLocal()
        snippet = fetch_snippet(db, name)

        if not snippet:
            return await interaction.response.send_message("❌ Not found", ephemeral=True)

        await interaction.response.send_message(f"```{snippet.content}```")

    @app_commands.command(name="snippet_delete", description="Delete a snippet")
    async def delete(self, interaction: discord.Interaction, name: str):
        db = SessionLocal()
        success = remove_snippet(db, name)

        msg = "Deleted" if success else "Not found"

        await interaction.response.send_message(msg, ephemeral=True)

    @app_commands.command(name="snippet_list", description="List snippets")
    async def list_snippets(self, interaction: discord.Interaction):
        db = SessionLocal()
        snippets = fetch_all_snippets(db)

        if not snippets:
            return await interaction.response.send_message("No snippets found")

        names = "\n".join([s.name for s in snippets])

        await interaction.response.send_message(f"**Snippets:**\n{names}")

async def setup(bot):
    await bot.add_cog(Snippet(bot))

import logging
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

# Initialize module logger
logger = logging.getLogger(__name__)

class Snippet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info("Snippet Cog initialized")

    @app_commands.command(name="snippet_create", description="Create a snippet")
    async def create(self, interaction: discord.Interaction, name: str, content: str):
        async with SessionLocal() as db: # Using the async_sessionmaker
            try:
                logger.info(f"User {interaction.user} (ID: {interaction.user.id}) is creating snippet: {name}")
                snippet = add_snippet(db, name, content, str(interaction.user.id))
            
                await interaction.response.send_message(
                f"✅ Snippet `{snippet.name}` created!",
                ephemeral=True
            )
            except Exception as e:
                logger.error(f"Failed to create snippet '{name}': {e}", exc_info=True)
                await interaction.response.send_message("❌ Failed to create snippet due to a database error.", ephemeral=True)
            finally:
                db.close()

    @app_commands.command(name="snippet_get", description="Get a snippet")
    async def get(self, interaction: discord.Interaction, name: str):
        async with SessionLocal() as db:
            try:
                snippet = fetch_snippet(db, name)

                if not snippet:
                    logger.warning(f"Snippet lookup failed: '{name}' requested by {interaction.user}")
                    return await interaction.response.send_message("❌ Not found", ephemeral=True)

                logger.info(f"Snippet '{name}' fetched by {interaction.user}")
                await interaction.response.send_message(f"```{snippet.content}```")
            except Exception as e:
                logger.error(f"Error fetching snippet '{name}': {e}", exc_info=True)
                await interaction.response.send_message("❌ An error occurred while retrieving the snippet.", ephemeral=True)
            finally:
                db.close()

    @app_commands.command(name="snippet_delete", description="Delete a snippet")
    async def delete(self, interaction: discord.Interaction, name: str):
        async with SessionLocal() as db:
            try:
                logger.info(f"User {interaction.user} attempting to delete snippet: {name}")
                success = remove_snippet(db, name)

                if success:
                    logger.info(f"Snippet '{name}' successfully deleted.")
                    await interaction.response.send_message(f"✅ Deleted snippet `{name}`", ephemeral=True)
                else:
                    logger.warning(f"Delete failed: Snippet '{name}' not found.")
                    await interaction.response.send_message("❌ Snippet not found.", ephemeral=True)
            except Exception as e:
                logger.error(f"Error deleting snippet '{name}': {e}", exc_info=True)
                await interaction.response.send_message("❌ Error occurred during deletion.", ephemeral=True)
            finally:
                db.close()

    @app_commands.command(name="snippet_list", description="List snippets")
    async def list_snippets(self, interaction: discord.Interaction):
        async with SessionLocal() as db:
            try:
                snippets = fetch_all_snippets(db)

                if not snippets:
                    return await interaction.response.send_message("No snippets found", ephemeral=True)

                logger.info(f"User {interaction.user} listed all snippets ({len(snippets)} found)")
                names = "\n".join([f"• {s.name}" for s in snippets])
                await interaction.response.send_message(f"**Available Snippets:**\n{names}")
            except Exception as e:
                logger.error(f"Error listing snippets: {e}", exc_info=True)
                await interaction.response.send_message("❌ Could not retrieve snippet list.", ephemeral=True)
            finally:
                db.close()

async def setup(bot):
    await bot.add_cog(Snippet(bot))

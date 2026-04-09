from discord.ext import commands
from discord import app_commands
import traceback

from utils.checks import is_owner
class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="reload", description="Reload a cog")
    @is_owner()
    async def reload(self, interaction, cog: str):
        await interaction.response.defer(ephemeral=True) # Defer because sync takes time
        try:
            await self.bot.reload_extension(f"cogs.{cog}")
            # Only sync if you actually changed the @app_commands structure
            await self.bot.tree.sync() 
            await interaction.followup.send(f"Reloaded `{cog}` and synced tree.")
        except Exception as e:
            await interaction.followup.send(f"Error: {e}")

    @app_commands.command(name="reload_all", description="Reload all cogs")
    @is_owner()
    async def reload_all(self, interaction):
        await interaction.response.defer(ephemeral=True)
        results = []

        for ext in list(self.bot.extensions):
            try:
                await self.bot.reload_extension(ext)
                results.append(f"{ext}")
            except Exception as e:
                results.append(f"{ext}: {e}")

        # SYNC ONCE HERE, AFTER THE LOOP
        await self.bot.tree.sync()
        
        await interaction.followup.send("\n".join(results))

    @app_commands.command(name="sync", description="Force sync the command tree")
    @is_owner()
    async def sync(self, interaction):
        """Dedicated sync command"""
        await interaction.response.defer(ephemeral=True)
        await self.bot.tree.sync()
        await interaction.followup.send("Tree synced!")

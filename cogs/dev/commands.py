from discord.ext import commands
from discord import app_commands
import traceback

from utils.checks import is_owner

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Reload single cog
    @app_commands.command(name="reload", description="Reload a cog")
    @app_commands.describe(cog="Cog path (e.g. user.commands)")
    @is_owner()
    async def reload(self, interaction, cog: str):
        try:
            await self.bot.reload_extension(f"cogs.{cog}")
            await interaction.response.send_message(f"✅ Reloaded `{cog}`")
            await self.bot.tree.sync()
        except Exception as e:
            error = "".join(traceback.format_exception(type(e), e, e.__traceback__))
            await interaction.response.send_message(f"❌ Error:\n```py\n{error[:1900]}\n```", ephemeral=True)

    # Reload ALL cogs
    @app_commands.command(name="reload_all", description="Reload all cogs")
    @is_owner()
    async def reload_all(self, interaction):
        results = []

        for ext in list(self.bot.extensions):
            try:
                await self.bot.reload_extension(ext)
                results.append(f"✅ {ext}")
                await self.bot.tree.sync()
            except Exception as e:
                results.append(f"❌ {ext}: {e}")

        await interaction.response.send_message("\n".join(results), ephemeral=True)

async def setup(bot):
    await bot.add_cog(Dev(bot))

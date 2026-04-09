from discord import guild
from discord.ext import commands
import discord 
from core.loader import load_extensions
# from database.db import engine, Base, SessionLocal
from config.settings import TOKEN,PREFIX,GUILD_ID

class ModularBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=discord.Intents.all()
        )

        

    async def setup_hook(self):
        await load_extensions(self)

        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        else:
            await self.tree.sync()

    def run(self):
        super().run(TOKEN)

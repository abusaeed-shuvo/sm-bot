import discord 
from discord.ext import commands
from core.loader import load_extensions
from config.settings import TOKEN, PREFIX, GUILD_ID

class ModularBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=discord.Intents.all()
        )
        self.dev_guild_id = GUILD_ID

    async def setup_hook(self):
        await load_extensions(self)
        print(f"Extensions loaded. Logged in as {self.user}")

    def run(self):
        super().run(TOKEN)

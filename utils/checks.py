from discord import app_commands
from config.settings import OWNER_ID

def is_owner():
    async def predicate(interaction):
        return interaction.user.id == OWNER_ID
    return app_commands.check(predicate)

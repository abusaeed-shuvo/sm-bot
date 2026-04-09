import logging
import os
from discord import app_commands
from config.settings import OWNER_ID

logger = logging.getLogger(__name__)

def is_owner():
    async def predicate(interaction):
        user_id = interaction.user.id
        # Log the comparison if it fails for easier debugging
        if user_id != OWNER_ID:
            logger.warning(f"Check failed: User {user_id} is not Owner {OWNER_ID}")
            return False
        return True
    return app_commands.check(predicate)

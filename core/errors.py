import logging

logger = logging.getLogger(__name__)

async def setup(bot):
    @bot.tree.error
    async def on_app_command_error(interaction, error):
        logger.error(f"Command error: {error}", exc_info=True)
        await interaction.response.send_message(
            f"Error: {error}",
            ephemeral=True
        )

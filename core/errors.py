async def setup(bot):
    @bot.tree.error
    async def on_app_command_error(interaction, error):
        await interaction.response.send_message(
            f"Error: {error}",
            ephemeral=True
        )

from dotenv import load_dotenv
import os


load_dotenv()


TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!") 
OWNER_ID = int(os.getenv("OWNER_ID", 0))
GUILD_ID = int(os.getenv("GUILD_ID", 0))

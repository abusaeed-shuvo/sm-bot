![Python](https://img.shields.io/badge/Python_3.11+-cba6f7?style=for-the-badge&logo=python&logoColor=1e1e2e)
![discord.py](https://img.shields.io/badge/discord.py-89b4fa?style=for-the-badge&logo=discord&logoColor=1e1e2e)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-f38ba8?style=for-the-badge)
![uv](https://img.shields.io/badge/uv-fast_env-a6e3a1?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-f9e2af?style=for-the-badge)
# sm-bot
Scalar Modular Discord Bot for easy modification and deployment

A scalable Discord bot template using slash commands and modular architecture.

## Features
- **Modular Architecture**: Organized into Cogs, Services, and Repositories.
- **Dependency Management**: Powered by `uv` for lightning-fast performance.
- **Database Support**: Built-in persistence for snippets and user data.
- **Slash Commands**: Modern Discord interactions.

## Setup

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
   ```
2. **Sync the project:**
   This will automatically create a virtual environment and install all dependencies from `pyproject.toml`.
   ```bash
   uv sync
   ```
3. **Configure Environment:**
   ```bash
   cp .env.example .env
   ```
   Add your bot token and database credentials to the .env file.
4. **Run the Bot:**
   ```bash
   uv run main.py
   ```

## Commands
- `/user` -> Get information about a user.

- `/avatar` -> Get a user's avatar.

- `/snippet` -> Manage text snippets (grouped commands).

## Project Structure
   This bot uses a structured design for better maintainability:

- `cogs/`: Command logic and listeners.

- `services/`: Business logic and data processing.

- `database/`: Repository patterns and SQLAlchemy models.

- `core/`: Bot initialization and error handling.

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
DISCORD_TOKEN=your_bot_token_here
DATABASE_URL=your_database_url_here
```

### Notes
- `DATABASE_URL` should be an async SQLAlchemy URL  
Example (SQLite):
```
sqlite+aiosqlite:///./data.db
```
Example (PostgreSQL):
```
postgresql+asyncpg://user:password@localhost/dbname
```

## Database Setup

Before running the bot, ensure the database is initialized:

```bash
uv run main.py
```

The bot will automatically create tables on startup using SQLAlchemy.

## Adding a New Cog

1. Create a new file inside `cogs/`
2. Define a Cog class
3. Add a setup function

Example:

```python
from discord.ext import commands

class Example(commands.Cog):
   def __init__(self, bot):
      self.bot = bot

async def setup(bot):
   await bot.add_cog(Example(bot))
```

The bot will automatically load all cogs at startup.

## Architecture Overview

- **Cogs** → Handle Discord commands and events  
- **Services** → Contain business logic  
- **Repositories** → Handle database access  
- **Models** → Define database schema  
- **Core** → Bot setup, loaders, and shared utilities  

Flow:
```
Cog → Service → Repository → Database
```

## Logging

Logs are written to the console and can be configured via Python's `logging` module.

You can modify log levels in the source code depending on your needs.

## Development

### Reloading Extensions
During development, you can reload cogs without restarting the bot (if implemented):

```
/reload <cog>
```

### Formatting
Recommended tools:
- `ruff` for linting
- `black` for formatting

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

Please ensure:
- Code is clean and formatted
- Features are modular
- No circular imports

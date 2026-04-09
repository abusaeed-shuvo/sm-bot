from pathlib import Path

async def load_extensions(bot):
    for path in Path("cogs").rglob("*.py"):
        if path.name == "__init__.py":
            continue

        module = ".".join(path.with_suffix("").parts)

        await bot.load_extension(module)

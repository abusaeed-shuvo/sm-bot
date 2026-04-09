import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from database.models.snippet import Snippet

logger = logging.getLogger(__name__)

async def create_snippet(db: AsyncSession, name: str, content: str, author_id: str):
    try:
        snippet = Snippet(name=name, content=content, author_id=author_id)
        db.add(snippet)
        await db.commit()  # Must be awaited
        await db.refresh(snippet)
        logger.debug(f"DB: Successfully committed new snippet '{name}'")
        return snippet
    except Exception as e:
        await db.rollback() # Must be awaited
        logger.error(f"DB Error during create_snippet: {e}")
        raise e

async def get_snippet(db: AsyncSession, name: str):
    # Async uses select() statements
    result = await db.execute(select(Snippet).filter_by(name=name))
    return result.scalars().first()

async def delete_snippet(db: AsyncSession, name: str):
    try:
        # Check if it exists first using our async getter
        snippet = await get_snippet(db, name)
        if snippet:
            await db.delete(snippet)
            await db.commit()
            logger.debug(f"DB: Successfully deleted snippet '{name}'")
            return True
        return False
    except Exception as e:
        await db.rollback()
        logger.error(f"DB Error during delete_snippet: {e}")
        raise e

async def list_snippets(db: AsyncSession):
    result = await db.execute(select(Snippet))
    return result.scalars().all()

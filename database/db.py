import logging
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config.settings import DATABASE_URL
from database.base import Base
from database.loader import load_models

logger = logging.getLogger(__name__)

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def init_db():
    try:
        load_models()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized and tables created.")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

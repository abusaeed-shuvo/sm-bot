from database.repository.snippet_repo import (
    create_snippet,
    get_snippet,
    delete_snippet,
    list_snippets
)

# Note: These are now all async functions
async def add_snippet(db, name, content, author_id):
    return await create_snippet(db, name, content, author_id)

async def fetch_snippet(db, name):
    return await get_snippet(db, name)

async def remove_snippet(db, name):
    return await delete_snippet(db, name)

async def fetch_all_snippets(db):
    return await list_snippets(db)

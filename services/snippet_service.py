from database.repository.snippet_repo import (
    create_snippet,
    get_snippet,
    delete_snippet,
    list_snippets
)

def add_snippet(db, name, content, author_id):
    return create_snippet(db, name, content, author_id)

def fetch_snippet(db, name):
    return get_snippet(db, name)

def remove_snippet(db, name):
    return delete_snippet(db, name)

def fetch_all_snippets(db):
    return list_snippets(db)

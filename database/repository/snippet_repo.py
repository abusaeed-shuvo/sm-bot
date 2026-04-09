from sqlalchemy.orm import Session
from database.models.snippet import Snippet

def create_snippet(db: Session, name: str, content: str, author_id: str):
    snippet = Snippet(name=name, content=content, author_id=author_id)
    db.add(snippet)
    db.commit()
    db.refresh(snippet)
    return snippet

def get_snippet(db: Session, name: str):
    return db.query(Snippet).filter_by(name=name).first()

def delete_snippet(db: Session, name: str):
    snippet = get_snippet(db, name)
    if snippet:
        db.delete(snippet)
        db.commit()
        return True
    return False

def list_snippets(db: Session):
    return db.query(Snippet).all()

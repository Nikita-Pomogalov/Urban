from .db import Session_local

async def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()
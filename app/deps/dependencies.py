from database.database import SessionLocal

def db_conn():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

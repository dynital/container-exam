import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError
from models import Base, User

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL non è impostata")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str


@app.get("/")
def api_root():
    return {"message": "OK"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health-db")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {"status": "ok", "message": "Database connection is healthy"}
    except OperationalError:
        raise HTTPException(status_code=500, detail="Database connection failed")        

@app.get("/users/")
def get_users():
    try:
        db = SessionLocal()
        users = db.query(User).all()
        return users
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        db.close()   

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()
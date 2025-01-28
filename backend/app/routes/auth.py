from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your_secret_key"

class UserAuth(BaseModel):
    username: str
    password: str

# Mock database
users_db = {}

@router.post("/register")
def register(user: UserAuth):
    hashed_password = pwd_context.hash(user.password)
    users_db[user.username] = hashed_password
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserAuth):
    if user.username not in users_db or not pwd_context.verify(user.password, users_db[user.username]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = jwt.encode({"sub": user.username}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}

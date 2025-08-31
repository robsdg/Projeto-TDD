from fastapi import FastAPI
from app.models import User
from app.crud import create_user, get_users

app = FastAPI()

@app.post("/users")
def add_user(user: User):
    return create_user(user)

@app.get("/users")
def list_users():
    return get_users()

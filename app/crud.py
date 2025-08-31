from app.database import users_collection
from app.models import User
from bson import ObjectId

def create_user(user: User) -> dict:
    user_dict = user.dict()
    result = users_collection.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

def get_users() -> list:
    users = []
    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

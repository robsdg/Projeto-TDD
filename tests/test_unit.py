from app.crud import create_user
from app.models import User

def test_create_user_unit(monkeypatch):
    # simula o insert_one do Mongo
    def fake_insert_one(data):
        class Result:
            inserted_id = "123456789"
        return Result()

    monkeypatch.setattr("app.crud.users_collection.insert_one", fake_insert_one)

    user = User(name="Robson", email="robson@email.com")
    result = create_user(user)

    assert result["name"] == "Robson"
    assert result["_id"] == "123456789"

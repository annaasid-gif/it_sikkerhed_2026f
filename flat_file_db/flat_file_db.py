import json
import os

DB_FILE = "database.json"

def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

def load_users():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def add_user(user):
    users = load_users()
    users.append(user)
    save_users(users)

def get_user(person_id):
    users = load_users()
    for u in users:
        if u["person_id"] == person_id:
            return u
    return None

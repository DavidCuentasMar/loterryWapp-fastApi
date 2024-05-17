from fastapi import APIRouter
from ..config.db import conn 
from ..models.user import User 
from ..schemas.user import serializeDict, serializeList
user_routes = APIRouter()

@user_routes.get('/user/all')
async def find_all_users():
    return serializeList(conn.local.user.find())

@user_routes.post('/user/')
async def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    conn.local.user.insert_one(new_user).inserted_id
    return serializeList(conn.local.user.find())
 
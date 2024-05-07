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
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())
 
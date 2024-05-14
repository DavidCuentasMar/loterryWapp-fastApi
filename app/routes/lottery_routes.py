from fastapi import APIRouter
from ..config.db import conn 
from ..models.lottery import Lottery
from ..models.user_lottery_junction import userLotteryJunction
from ..schemas.lottery import serializeDict, serializeList
from ..schemas.user_lottery_junction import serializeDict, serializeList
from bson import ObjectId
from datetime import datetime
lottery_routes = APIRouter()

@lottery_routes.get('/lottery/all')
async def find_all_lotteries():
    return serializeList(conn.local.lottery.find())

@lottery_routes.post('/lottery/')
async def create_lottery(lottery: Lottery):
    if(lottery.number is None):
        lottery.number = -1
    if(lottery.completed is None):
        lottery.completed = False
    lottery.create_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.local.lottery.insert_one(dict(lottery))
    return serializeList(conn.local.lottery.find())

@lottery_routes.get('/lottery/{id}')
async def get_lottery(id,lottery: Lottery):
    conn.local.lottery.find_one({"_id":ObjectId(id)})
    return serializeDict(conn.local.lottery.find_one({"_id":ObjectId(id)}))

@lottery_routes.post('/lottery/{id}/participation/')
async def create_lottery_participation(user_lottery_junction_obj: userLotteryJunction):
    #Validate existance of lottery and user
    #TO-DO: bson.errors.InvalidId: '6636550633f20fc6bd39455' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string
    lottery_obj = conn.local.lottery.find_one({"_id":ObjectId(user_lottery_junction_obj.lotteryId)})
    user_obj = conn.local.user.find_one({"_id":ObjectId(user_lottery_junction_obj.userId)})
    if lottery_obj is None:
        return {'message':'lottery not found'}
    if user_obj is None:
        return {'message':'user not found'}        
    user_lottery_junction_obj = conn.local.userLotteryJunction.insert_one(dict(user_lottery_junction_obj))
    return serializeDict(conn.local.userLotteryJunction.find_one({"_id":ObjectId(user_lottery_junction_obj.inserted_id)}))

@lottery_routes.get('/lottery/{id}/participation/all')
async def get_lottery_participation(id):
    user_lottery_junction_list = conn.local.userLotteryJunction.find({"lotteryId":id})
    return serializeList(user_lottery_junction_list)

@lottery_routes.delete('/lottery/{id}/participation/{participation_id}')
async def delete_lottery_participation(id, participation_id):
    user_lottery_junction_list = conn.local.userLotteryJunction.find_one_and_delete({"_id":ObjectId(participation_id)})
    if user_lottery_junction_list is None:
        return {'message':'participation not found'}    
    return serializeDict(user_lottery_junction_list)
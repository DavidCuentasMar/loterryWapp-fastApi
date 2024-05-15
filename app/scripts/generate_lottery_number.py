from ..config.db import conn 
from ..schemas.lottery import serializeDict, serializeList
from ..schemas.user_lottery_junction import serializeDict, serializeList
from bson import ObjectId
import random

def generate_lottery_number():
    lotteryList = serializeList(conn.local.lottery.find({"number":-1, "completed": False}).sort({"create_datetime": -1}).limit(1))
    if(len(lotteryList)>0):
        lottery_number = random.randint(0, 34563)
        lottery = lotteryList[0]
        data = {}
        data['completed'] = True
        data['number'] = lottery_number
        userList = serializeList(conn.local.userLotteryJunction.find({"number":lottery_number}))
        if(len(userList)>0):
            winner = userList[0]
            data['winner'] = winner['_id']
            conn.local.lottery.update_one({"_id": ObjectId(lottery['_id'])},{"$set":data})
    else:
        print("No active lotteries")
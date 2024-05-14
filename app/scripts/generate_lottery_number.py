from ..config.db import conn 
from ..schemas.lottery import serializeDict, serializeList
from bson import ObjectId
import random

def generate_lottery_number():
    lotteryList = serializeList(conn.local.lottery.find({"number":-1, "completed": False}).sort({"create_datetime": -1}).limit(1))
    if(len(lotteryList)>0):
        lottery = lotteryList[0]
        data = {}
        data['completed'] = True
        data['number'] = random.randint(0, 34563)
        conn.local.lottery.update_one({"_id": ObjectId(lottery['_id'])},{"$set":data})
    else:
        print("No active lotteries")
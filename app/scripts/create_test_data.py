# python -m app.scripts.create_test_data
from ..config.db import conn 
from ..models.user import User
from ..models.lottery import Lottery
from ..models.user_lottery_junction import userLotteryJunction
from datetime import datetime

import json
import random
import os


user_list = []
lottery_list = []
participation_list = []
clear_collections = True

if clear_collections:
    conn.local.user.drop()
    conn.local.lottery.drop()
    conn.local.userLotteryJunction.drop()

for x in range(10):
    user_name = 'user' + str(x)
    user_email = user_name + '@email.com'
    json_str = '{"name":"'+user_name+'","email":"'+user_email+'","password":"123"}'
    json_object = json.loads(json_str)
    user_list.append(conn.local.user.insert_one(dict(json_object)))

for x in range(3):
    data = {}
    data['name'] = 'lottery #' + str(x)
    data['number'] = -1
    data['completed'] = False
    data['created_datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lottery_list.append(conn.local.lottery.insert_one(data))

for x in range(10):
    user_id = user_list[x].inserted_id
    lottery_id = lottery_list[random.randint(0, len(lottery_list)-1)].inserted_id
    number = random.randint(0, os.getenv("LIMIT_RANDOM_NUMBER", -1))
    data = {}
    data['userId'] = str(user_id)
    data['lotteryId'] = str(lottery_id)
    data['number'] = number
    conn.local.userLotteryJunction.insert_one(data)    
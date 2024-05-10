# python -m app.scripts.create_test_data
from ..config.db import conn 
from ..models.user import User
from ..models.lottery import Lottery
from ..models.user_lottery_junction import userLotteryJunction

import json
import random

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

for x in range(10):
    lottery_name = 'lottery #' + str(x)
    json_str = '{"name":"'+lottery_name+'"}'
    json_object = json.loads(json_str)
    lottery_list.append(conn.local.lottery.insert_one(dict(json_object)))

for x in range(10):
    user_id = user_list[x].inserted_id
    lottery_id = lottery_list[x].inserted_id
    number = random.randint(0, 34563)
    json_str = '{"userId":"'+str(user_id)+'","lotteryId":"'+str(lottery_id)+'","number":'+str(number)+'}'
    json_object = json.loads(json_str)
    conn.local.userLotteryJunction.insert_one(dict(json_object))    
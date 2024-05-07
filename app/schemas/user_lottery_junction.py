# Normal way
def userLotteryJunctionEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "userId":item["userId"],
        "lotteryId":item["lotteryId"],
        "number":item["number"]
    }

def userLotteryJunctionEntity(entity) -> list:
    return [userLotteryJunctionEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
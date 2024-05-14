# Normal way
def lotteryEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "number":item["number"],
        "completed":item["completed"]
    }

def lotteryEntity(entity) -> list:
    return [lotteryEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
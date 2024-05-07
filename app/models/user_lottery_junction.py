from pydantic import BaseModel

class userLotteryJunction(BaseModel):
    userId: str
    lotteryId: str
    number: int

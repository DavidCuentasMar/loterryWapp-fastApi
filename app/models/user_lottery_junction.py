from pydantic import BaseModel
from typing import Optional

class userLotteryJunction(BaseModel):
    id: Optional[str]
    userId: str
    lotteryId: str
    number: int

from datetime import datetime

from pydantic import BaseModel


class Judgements(BaseModel):
    perfect: int
    great: int
    good: int
    miss: int


class Score(BaseModel):
    identifier: str
    matchType: str
    lamp: str
    difficulty: str
    percent: float
    judgements: Judgements
    timeAchieved: int = int(datetime.now().timestamp())

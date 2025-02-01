import dataclasses
from dataclasses import dataclass
from datetime import datetime
import json
from typing import Any


@dataclass
class Judgements:
    perfect: int
    great: int
    good: int
    miss: int


@dataclass
class Score:
    identifier: str
    matchType: str
    lamp: str
    difficulty: str
    percent: float
    judgements: Judgements
    timeAchieved: int = int(datetime.now().timestamp())


class ScoreDataclassEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

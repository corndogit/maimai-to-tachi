from enum import Enum

from pydantic import BaseModel


class DanRankStatus(str, Enum):
    UNPLAYED = "Unplayed",
    FAILED = "Failed",
    CLEARED = "Cleared"


class DanRank(BaseModel):
    name: str
    display_name: str
    status: DanRankStatus = DanRankStatus.UNPLAYED

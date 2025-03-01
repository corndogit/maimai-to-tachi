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


dan_ranks = {
    "DAN_1": DanRank(name="DAN_1", display_name="1st Dan"),
    "DAN_2": DanRank(name="DAN_2", display_name="2nd Dan"),
    "DAN_3": DanRank(name="DAN_3", display_name="3rd Dan"),
    "DAN_4": DanRank(name="DAN_4", display_name="4th Dan"),
    "DAN_5": DanRank(name="DAN_5", display_name="5th Dan"),
    "DAN_6": DanRank(name="DAN_6", display_name="6th Dan", status=DanRankStatus.CLEARED),
    "DAN_7": DanRank(name="DAN_7", display_name="7th Dan"),
    "DAN_8": DanRank(name="DAN_8", display_name="8th Dan"),
    "DAN_9": DanRank(name="DAN_9", display_name="9th Dan"),
    "DAN_10": DanRank(name="DAN_10", display_name="10th Dan"),
    "KAIDEN": DanRank(name="KAIDEN", display_name="Grade MG"),
    "SHINDAN_1": DanRank(name="SHINDAN_1", display_name="1st Shindan"),
    "SHINDAN_2": DanRank(name="SHINDAN_2", display_name="2nd Shindan"),
    "SHINDAN_3": DanRank(name="SHINDAN_3", display_name="3rd Shindan"),
    "SHINDAN_4": DanRank(name="SHINDAN_4", display_name="4th Shindan"),
    "SHINDAN_5": DanRank(name="SHINDAN_5", display_name="5th Shindan"),
    "SHINDAN_6": DanRank(name="SHINDAN_6", display_name="6th Shindan"),
    "SHINDAN_7": DanRank(name="SHINDAN_7", display_name="7th Shindan"),
    "SHINDAN_8": DanRank(name="SHINDAN_8", display_name="8th Shindan"),
    "SHINDAN_9": DanRank(name="SHINDAN_9", display_name="9th Shindan"),
    "SHINDAN_10": DanRank(name="SHINDAN_10", display_name="10th Shindan"),
    "SHINKAIDEN": DanRank(name="SHINKAIDEN", display_name="Shindan MG"),
    "URASHINKAIDEN": DanRank(name="URASHINKAIDEN", display_name="Ura Kaiden"),
}

from dataclasses import dataclass
from enum import Enum


class DanRankStatus(str, Enum):
    UNPLAYED = "Unplayed",
    FAILED = "Failed",
    CLEARED = "Cleared"

    def __str__(self) -> str:
        return self.value


@dataclass
class DanRank:
    name: str
    display_name: str
    cell_value: str

    def __repr__(self) -> str:
        return self.display_name


dan_ranks = [
    DanRank("DAN_1",      "1st Dan",      "C2"),
    DanRank("DAN_2",      "2nd Dan",      "I2"),
    DanRank("DAN_3",      "3rd Dan",      "O2"),
    DanRank("DAN_4",      "4th Dan",      "C9"),
    DanRank("DAN_5",      "5th Dan",      "I9"),
    DanRank("DAN_6",      "6th Dan",      "O9"),
    DanRank("DAN_7",      "7th Dan",      "C16"),
    DanRank("DAN_8",      "8th Dan",      "I16"),
    DanRank("DAN_9",      "9th Dan",      "O16"),
    DanRank("DAN_10",     "10th Dan",     "C23"),
    DanRank("KAIDEN",     "Grade MG",     "I23"),
]


shindan_ranks = [  # unsupported but here for completion
    DanRank("SHINDAN_1",  "1st Shindan",  "C31"),
    DanRank("SHINDAN_2",  "2nd Shindan",  "I31"),
    DanRank("SHINDAN_3",  "3rd Shindan",  "O31"),
    DanRank("SHINDAN_4",  "4th Shindan",  "C38"),
    DanRank("SHINDAN_5",  "5th Shindan",  "I38"),
    DanRank("SHINDAN_6",  "6th Shindan",  "O38"),
    DanRank("SHINDAN_7",  "7th Shindan",  "C45"),
    DanRank("SHINDAN_8",  "8th Shindan",  "I45"),
    DanRank("SHINDAN_9",  "9th Shindan",  "O45"),
    DanRank("SHINDAN_10", "10th Shindan", "C52"),
    DanRank("SHINKAIDEN", "Shindan MG",   "I52"),
]

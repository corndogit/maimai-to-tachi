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


dan_ranks = [
    DanRank("1_DAN",      "1st Dan",      "C2"),
    DanRank("2_DAN",      "2nd Dan",      "I2"),
    DanRank("3_DAN",      "3rd Dan",      "O2"),
    DanRank("4_DAN",      "4th Dan",      "C9"),
    DanRank("5_DAN",      "5th Dan",      "I9"),
    DanRank("6_DAN",      "6th Dan",      "O9"),
    DanRank("7_DAN",      "7th Dan",      "C16"),
    DanRank("8_DAN",      "8th Dan",      "I16"),
    DanRank("9_DAN",      "9th Dan",      "O16"),
    DanRank("10_DAN",     "10th Dan",     "C23"),
    DanRank("KAIDEN",     "Grade MG",     "I23"),
]


shindan_ranks = [
    DanRank("1_SHINDAN",  "1st Shindan",  "C31"),
    DanRank("2_SHINDAN",  "2nd Shindan",  "I31"),
    DanRank("3_SHINDAN",  "3rd Shindan",  "O31"),
    DanRank("4_SHINDAN",  "4th Shindan",  "C38"),
    DanRank("5_SHINDAN",  "5th Shindan",  "I38"),
    DanRank("6_SHINDAN",  "6th Shindan",  "O38"),
    DanRank("7_SHINDAN",  "7th Shindan",  "C45"),
    DanRank("8_SHINDAN",  "8th Shindan",  "I45"),
    DanRank("9_SHINDAN",  "9th Shindan",  "O45"),
    DanRank("10_SHINDAN", "10th Shindan", "C52"),
    DanRank("SHINKAIDEN", "Shindan MG",   "I52"),
]

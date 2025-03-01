from enum import Enum


class Difficulty(str, Enum):
    BASIC = "Basic"
    ADVANCED = "Advanced"
    EXPERT = "Expert"
    MASTER = "Master"
    RE_MASTER = "Re:Master"

from dataclasses import dataclass


@dataclass
class Difficulty:
    name: str
    last_row: int


difficulties = [
    Difficulty('Basic', 634),
    Difficulty('Advanced', 634),
    Difficulty('Expert', 634),
    Difficulty('Master', 634),
    Difficulty('Re:Master', 77)
]

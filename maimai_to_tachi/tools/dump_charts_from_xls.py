import json
from os import PathLike
from typing import Any
import pandas as pd
from pathlib import Path

sheet_names = ["Basic", "Advanced", "Expert", "Master", "ReMaster"]
excel_path = Path.cwd() / "downloads" / "maimai Finale Score - corndog v5.1.2.xlsx"  # not in repo


def get_joined_dataframes() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for sn in sheet_names:
        sheet = pd.read_excel(excel_path, sheet_name=sn)
        diff_series = pd.Series([sn for _ in range(len(sheet))])
        sheet["Difficulty"] = diff_series
        frames.append(sheet)
    return pd.concat(frames)


def write_to_file(charts: list, path: PathLike) -> None:
    with open(path, 'w') as file:
        json.dump(charts, file)


def main() -> None:
    df: pd.DataFrame = get_joined_dataframes()
    df_slice = df[["ID", "Category", "Song", "Diff", "Difficulty",
                   "CC", "Notes", "Tap", "Hold", "Slide", "Break"]]
    charts: list[dict[str, Any]] = []
    for row in df_slice.itertuples():
        charts.append({
            "id": row.ID,
            "song": str(row.Song),  # because of "39" rofl
            "category": row.Category,
            "difficulty": row.Difficulty,
            "level": str(row.Diff),
            "chartConstant": row.CC,
            "notes": row.Notes,
            "tap": row.Tap,
            "hold": row.Hold,
            "slide": row.Slide,
            "break": row.Break
        })
    write_to_file(charts, excel_path.parent / "chart_dump.json")


if __name__ == "__main__":
    main()

import json
from typing import Iterable
from dacite import from_dict

import gspread
from gspread.spreadsheet import Spreadsheet

from maimai_to_tachi import config, logging_config
from maimai_to_tachi.difficulty import difficulties
from maimai_to_tachi.score import Score

logger = logging_config.get_logger(__name__)


def _read_scores_from_sheet(sheet: Spreadsheet) -> list[Score]:
    scores = []
    for diff in difficulties:
        tachi_codes = list(sheet.worksheet(
            diff.name).get(f"U2:U{diff.last_row}"))
        _map_and_append_scores(scores, tachi_codes)
    return scores


def _map_and_append_scores(
        scores: list[Score],
        tachi_codes: list[Iterable]
) -> list[Score]:
    for t in tachi_codes:
        if t != []:
            score = from_dict(data_class=Score, data=json.loads(t[0].rstrip(',')))
            if score.judgements.miss > 0:
                score.lamp = "CLEAR"
            scores.append(score)


def get_scores_from_maimai_spreadsheet() -> list[Score]:
    gc = gspread.service_account(config.service_account_creds_path)
    logger.info(f"Opening {config.sheet_title} from Google Sheets")
    sh = gc.open(config.sheet_title)
    scores = _read_scores_from_sheet(sh)
    logger.info(f"Adding {len(scores)} scores to request payload")
    return scores

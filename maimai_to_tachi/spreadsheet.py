import json
from typing import Iterable, Any
from dacite import from_dict

import gspread
from gspread.spreadsheet import Spreadsheet

from maimai_to_tachi import logging_config
from maimai_to_tachi.config import ScriptConfig
from maimai_to_tachi.dataclasses.difficulty import difficulties
from maimai_to_tachi.dataclasses.score import Score

logger = logging_config.get_logger(__name__)
config = ScriptConfig.create()


def _read_scores_from_sheet(sheet: Spreadsheet) -> list[Score]:
    scores = []
    for diff in difficulties:
        tachi_codes = list(sheet.worksheet(
            diff.name).get(f"U2:U{diff.last_row}"))
        _map_and_append_scores(scores, tachi_codes)
    return scores


def _parse_tachi_code(code: Iterable) -> Any:
    try:
        return json.loads(code)
    except json.JSONDecodeError:
        raise ValueError(f"Failed to parse the following Tachi code: {code}")


def _map_and_append_scores(
        scores: list[Score],
        tachi_codes: list[Iterable]
) -> list[Score]:
    ignored_codes = []
    for t in tachi_codes:
        if t is not None and t != []:
            code = t[0].rstrip(',')
            try:
                tachi_code_object = _parse_tachi_code(code)
            except ValueError:
                logger.warning(f"Could not parse code, skipping: {code}")
                ignored_codes.append(code)
            score = from_dict(data_class=Score,
                              data=tachi_code_object)
            if score.judgements.miss > 0:
                score.lamp = "CLEAR"
            scores.append(score)
    if len(ignored_codes) > 0:
        logger.warning(f"{len(ignored_codes)} score(s) skipped due to parsing errors")


def get_scores_from_maimai_spreadsheet() -> list[Score]:
    gc = gspread.service_account(config.service_account_creds_path)
    logger.info(f"Opening {config.sheet_title} from Google Sheets")
    sh = gc.open(config.sheet_title)
    scores = _read_scores_from_sheet(sh)
    logger.info(f"Adding {len(scores)} scores to request payload")
    return scores

import json
from pathlib import Path
from typing import Iterable, Any
from dacite import from_dict

import gspread
from gspread.spreadsheet import Spreadsheet

from maimai_to_tachi import logging_config
from maimai_to_tachi.config import ScriptConfig
from maimai_to_tachi.dataclasses.dan_rank import DanRank, DanRankStatus, dan_ranks
from maimai_to_tachi.dataclasses.difficulty import difficulties
from maimai_to_tachi.dataclasses.score import Score

logger = logging_config.get_logger(__name__)
config = ScriptConfig.create()


def get_spreadsheet(sheet_title: str, service_account_creds_path: Path) -> Spreadsheet:
    gc = gspread.service_account(service_account_creds_path)
    logger.info(f"Opening {sheet_title} from Google Sheets")
    return gc.open(sheet_title)


def get_scores_from_maimai_spreadsheet(sheet: Spreadsheet) -> list[Score]:
    scores: list[Score] = []
    for diff in difficulties:
        logger.debug(f"Finding {diff.name} scores...")
        tachi_codes = list(sheet.worksheet(
            diff.name).get(f"U2:U{diff.last_row}"))
        _map_and_append_scores(scores, tachi_codes)
    logger.info(f"Adding {len(scores)} scores to request payload")
    return scores


def get_highest_dan_rank_from_maimai_spreadsheet(
    sheet: Spreadsheet
) -> DanRank | None:
    rank_cell_value_ranges = sheet.worksheet("Course").batch_get(
        [dan_rank.cell_value for dan_rank in dan_ranks]
    )
    results = list(zip(dan_ranks, rank_cell_value_ranges))
    ranks = list(filter(
        lambda dr: dr[1].first() == DanRankStatus.CLEARED,
        results
    ))
    log_message = f"Found {len(ranks)} cleared dan ranks"
    if len(ranks) > 0:
        highest_rank = ranks[0][0]
        log_message += f"- highest achieved is {highest_rank.display_name}"
    logger.info(log_message)
    return highest_rank if len(ranks) > 0 else None


def _parse_tachi_code(code: Iterable) -> Any:
    try:
        return json.loads(str(code))
    except json.JSONDecodeError:
        raise ValueError(f"Failed to parse the following Tachi code: {code}")


def _map_and_append_scores(
        scores: list[Score],
        tachi_codes: list[Iterable]
) -> None:
    ignored_codes = []
    appended_count = 0
    for t in tachi_codes:
        if t is not None and t != []:
            code = list(t)[0].rstrip(',')
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
            appended_count += 1
    logger.debug(f"{appended_count} score(s) appended to request body")
    if len(ignored_codes) > 0:
        logger.warning(f"{len(ignored_codes)} score(s) skipped due to parsing errors")

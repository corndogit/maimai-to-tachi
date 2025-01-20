import json
from typing import Any

import gspread
from gspread.spreadsheet import Spreadsheet

from maimai_to_tachi import config, logging_config
from maimai_to_tachi.difficulty import difficulties

logger = logging_config.get_logger(__name__)


def _read_scores_from_sheet(sheet: Spreadsheet) -> list[Any]:
  scores = []
  for diff in difficulties:
    tachi_codes = list(sheet.worksheet(diff.name).get(f"U2:U{diff.last_row}"))
    for t in tachi_codes:
      if t != []:
        scores.append(json.loads(t[0].rstrip(',')))
  return scores


def get_scores_from_maimai_spreadsheet() -> list[Any]:
  gc = gspread.service_account(config.service_account_creds_path)
  logger.info(f"Opening {config.sheet_title} from Google Sheets")
  sh = gc.open(config.sheet_title)
  scores = _read_scores_from_sheet(sh)
  logger.info(f"Adding {len(scores)} scores to request payload")
  return scores

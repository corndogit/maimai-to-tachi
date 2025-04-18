import json
from pathlib import Path
import sys
from datetime import datetime
from typing import Any

import requests
from requests.exceptions import (ConnectionError, HTTPError, RequestException,
                                 Timeout)

from maimai_to_tachi import logging_config
from maimai_to_tachi.dataclasses.dan_rank import DanRank
from maimai_to_tachi.dataclasses.score import ScoreDataclassEncoder

logger = logging_config.get_logger(__name__)

TACHI_IMPORT_ENDPOINT = "https://kamai.tachi.ac/ir/direct-manual/import"
TACHI_IMPORT_REQUEST_BODY = {
    "meta": {"game": "maimai", "service": "manual", "playtype": "Single"},
    "scores": [],
}


def _write_to_file(
        output_dir: Path,
        request_body: dict[str, Any],
        filename: str = "output.json",
) -> None:
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_dir / filename, "w") as file:
        json.dump(request_body, file, cls=ScoreDataclassEncoder)


def save_local_copy(output_dir: Path, request_body: dict[str, Any]) -> None:
    try:
        filename = f"maimai-scores-{int(datetime.now().timestamp())}.json"
        _write_to_file(output_dir, request_body, filename)
        logger.info(f"Saved to JSON file at {output_dir}")
    except Exception as e:
        logger.error(f"Could not save file: {e}")
        sys.exit(1)


def submit_scores(tachi_api_key: str, request_body: dict[str, Any]) -> None:
    headers = {
        "Authorization": f"Bearer {tachi_api_key}",
        "X-User-Intent": "ir/direct-manual",
    }
    try:
        score_payload = json.loads(json.dumps(
            request_body, cls=ScoreDataclassEncoder))  # this sucks
        response = requests.post(
            TACHI_IMPORT_ENDPOINT,
            json=score_payload,
            headers=headers,
            timeout=15
        )
        response.raise_for_status()
        logger.info("Scores submitted to Kamaitachi")
    except ConnectionError:
        logger.error("Failed to connect to the server.")
    except Timeout:
        logger.error("The request timed out.")
    except HTTPError as http_err:
        logger.error(f"HTTP error: {http_err}")
    except RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")


def add_scores_to_request_body(
        scores: list[Any],
        dan_rank: DanRank | None = None
) -> dict[str, Any]:
    request_body = TACHI_IMPORT_REQUEST_BODY
    request_body["scores"] = scores
    if dan_rank is not None:
        request_body["classes"] = {"dan": dan_rank.name}
    return request_body

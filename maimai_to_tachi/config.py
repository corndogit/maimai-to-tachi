import sys
import tomllib
import webbrowser
from pathlib import Path

from maimai_to_tachi import logging_config

logger = logging_config.get_logger(__name__)

CONFIG_TEMPLATE = f"""### User config for maimai-to-tachi
# sheet_title: Title of the maimai Finale spreadsheet in your Google Drive
# tachi_api_key: API key with permissions to submit scores to Kamaitachi (optional)
# output_dir: Where output JSON is saved. Defaults to ~/maimai-to-tachi

[user]
sheet_title = ""
tachi_api_key = ""
output_dir = "{Path(Path.home() / 'maimai-to-tachi').as_posix()}"
"""

config_dir: Path = Path.home() / ".config" / "maimai-to-tachi"
config_path: Path = config_dir / "config.toml"
service_account_creds_path: Path = config_dir / "service_account.json"
config_invalid = False
sheet_title: str
tachi_api_key: str
output_dir: Path

if not config_path.exists():
    config_dir.mkdir(parents=True, exist_ok=True)
    with open(config_path, 'w') as file:
        file.write(CONFIG_TEMPLATE)
        logger.info("Created a new config file at %s" % config_path)
        config_invalid = True

if not service_account_creds_path.exists():
    logger.fatal("No service account credentials file found at %s. Please add "
                 "the file and try again." %
                 service_account_creds_path)
    config_invalid = True
    sys.exit(1)

if not config_invalid:
    try:
        with open(config_path, 'rb') as file:
            config_file = tomllib.load(file)

        sheet_title = config_file['user']['sheet_title']
        tachi_api_key = config_file['user']['tachi_api_key']
        output_dir = Path(config_file['user']['output_dir'])
    except Exception as e:
        e.add_note("Failed to read and set config: %s" % e)
        raise e
else:
    webbrowser.open(config_path)

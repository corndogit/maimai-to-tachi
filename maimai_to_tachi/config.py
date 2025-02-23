import tomllib
from typing import Type
import webbrowser
from pathlib import Path

from maimai_to_tachi import logging_config

logger = logging_config.get_logger(__name__)

DEFAULT_CONFIG_DIR = Path.home() / ".config" / "maimai-to-tachi"
CONFIG_TEMPLATE = f"""### User config for maimai-to-tachi
# sheet_title: Title of the maimai Finale spreadsheet in your Google Drive
# tachi_api_key: API key with permissions to submit scores to Kamaitachi (optional)
# output_dir: Where output JSON is saved. Defaults to ~/maimai-to-tachi

[user]
sheet_title = ""
tachi_api_key = ""
output_dir = "{Path(Path.home() / 'maimai-to-tachi').as_posix()}"
"""


class ScriptConfig:
    def __init__(self) -> None:
        self.config_path: Path
        self.service_account_creds_path: Path
        self.invalid: bool
        self.sheet_title: str
        self.tachi_api_key: str
        self.output_dir: Path

    @classmethod
    def create(
        cls: Type['ScriptConfig'],
        config_path: Path = DEFAULT_CONFIG_DIR / "config.toml",
        service_account_creds_path: Path = DEFAULT_CONFIG_DIR / "service_account.json",
        skip_init: bool = False,
        generate_config: bool = True
    ) -> 'ScriptConfig':
        config = cls()
        config.config_path = config_path
        config.service_account_creds_path = service_account_creds_path
        if not skip_init:
            config._config_file_exists(generate_config)
            config._service_account_creds_exists()
            config._set_config()
        return config

    def _config_file_exists(self, generate_config: bool = True) -> None:
        if not self.config_path.exists():
            no_config_warning = f"No config file found at {self.config_path.absolute()}"
            logger.warning(no_config_warning)
            if generate_config:
                self._generate_config_template()
            else:
                raise FileNotFoundError(no_config_warning)

    def _generate_config_template(self) -> None:
        self.config_dir.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w') as file:
            file.write(CONFIG_TEMPLATE)
            logger.info("Created a new config file at %s" % self.config_path)
        webbrowser.open(self.config_path)

    def _service_account_creds_exists(self) -> None:
        if not self.service_account_creds_path.exists():
            logger.warning("No service account credentials file found at %s."
                           "Google Sheets operations will not work!" %
                           self.service_account_creds_path)

    def _set_config(self) -> None:
        try:
            with open(self.config_path, 'rb') as file:
                config_file = tomllib.load(file)

            self.sheet_title = config_file['user']['sheet_title']
            self.tachi_api_key = config_file['user']['tachi_api_key']
            self.output_dir = Path(config_file['user']['output_dir'])
        except Exception as e:
            e.add_note("Failed to read and set config: %s" % e)
            raise e

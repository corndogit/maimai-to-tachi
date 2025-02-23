from maimai_to_tachi import spreadsheet, tachi
from maimai_to_tachi.config import ScriptConfig

# A script that when executed will:
# - Get the spreadsheet from Google Sheets for the configured user
# - Build and send a request object to Kamaitachi
# - Optionally save a backup of scores to a JSON file

if __name__ == "__main__":
    config = ScriptConfig.create()
    scores_from_sheet = spreadsheet.get_scores_from_maimai_spreadsheet(
        config.sheet_title,
        config.service_account_creds_path
    )
    scores_request = tachi.add_scores_to_request_body(scores_from_sheet)

    tachi.save_local_copy(config.output_dir, scores_request)
    tachi.submit_scores(config.tachi_api_key, scores_request)

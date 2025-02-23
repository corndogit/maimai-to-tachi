from maimai_to_tachi import spreadsheet, tachi
from maimai_to_tachi.config import ScriptConfig

# A script that when executed will:
# - Get the spreadsheet from Google Sheets for the configured user
# - Build and send a request object to Kamaitachi
# - Optionally save a backup of scores to a JSON file

if __name__ == "__main__":
    config = ScriptConfig.create()
    sheet = spreadsheet.get_spreadsheet(
        config.sheet_title,
        config.service_account_creds_path)
    scores = spreadsheet.get_scores_from_maimai_spreadsheet(sheet)
    dan_rank = spreadsheet.get_highest_dan_rank_from_maimai_spreadsheet(sheet)
    scores_request = tachi.add_scores_to_request_body(scores, dan_rank)

    tachi.save_local_copy(config.output_dir, scores_request)
    tachi.submit_scores(config.tachi_api_key, scores_request)

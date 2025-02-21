from maimai_to_tachi import spreadsheet, tachi

# A script that when executed will:
# - Get the spreadsheet from Google Sheets for the configured user
# - Build and send a request object to Kamaitachi
# - Optionally save a backup of scores to a JSON file

if __name__ == "__main__":
    scores_from_sheet = spreadsheet.get_scores_from_maimai_spreadsheet()
    scores_request = tachi.add_scores_to_request_body(scores_from_sheet)

    tachi.save_local_copy(scores_request)
    tachi.submit_scores(scores_request)

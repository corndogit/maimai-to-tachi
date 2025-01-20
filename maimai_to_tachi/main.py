from maimai_to_tachi import spreadsheet, tachi

if __name__ == "__main__":
  scores_from_sheet = spreadsheet.get_scores_from_maimai_spreadsheet()
  scores_request = tachi.add_scores_to_request_body(scores_from_sheet)

  tachi.save_local_copy(scores_request)
  tachi.submit_scores(scores_request)

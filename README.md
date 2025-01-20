# maimai-to-tachi

A script for exporting scores from the [maimai Finale score spreadsheet](https://docs.google.com/spreadsheets/d/1fsbC9Fi9W1IH0wG4p--YQ0kAcTKMGgQehj75ybvOles) by Iamuss76. Currently only the lite version is supported.

Scores can be saved locally to a JSON file for manually importing into arcade score trackers such as Kamaitachi. The script can also automatically POST a score import to Kamaitachi on your behalf.

It's still very much a work in progress and I hope to make it more user-friendly in future versions.

## Requirements

- Python >=3.10
- Poetry (optional)
- Google Dev Cloud service account to read from Google Sheets
- Kamaitachi API key with `submit_scores` permission

## Instructions



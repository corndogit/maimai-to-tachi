# Maimai to Tachi API

This API intends to serve as the backend for a web app that will allow users to enter scores,
save them to a database and create a JSON file that can be downloaded and manually imported into Kamaitachi.

Dependencies are defined in the main `pyproject.toml` file. To start the dev server with poetry, run:

```bash
poetry run fastapi dev main_api.py
```

This will start a server on http://127.0.0.1:8000. Swagger docs are also auto-generated and available at http://127.0.0.1:8000/docs.

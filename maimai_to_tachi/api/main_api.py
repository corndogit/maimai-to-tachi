from fastapi import FastAPI
from maimai_to_tachi.api.routers import dev

app = FastAPI()
app.include_router(dev.router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"information": "MaiMai FiNALE Score Tracker"}

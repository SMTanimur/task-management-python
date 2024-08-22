from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

app = FastAPI(title="Tast management", version="0.1.0")


@app.get("/", tags=["Root"])
async def root() -> dict:
    # print(settings.DATABASE_URL)
    return {"message": "Assalamua Alaikum, Welcome to the Task management API"}



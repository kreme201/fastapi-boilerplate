from fastapi import FastAPI

from app.database.middlwares import SqlAlchemySessionMiddleware

app = FastAPI()

app.add_middleware(SqlAlchemySessionMiddleware)


@app.get("/")
def index():
    return {
        "message": "Hello World",
    }

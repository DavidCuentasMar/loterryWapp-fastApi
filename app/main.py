from fastapi import FastAPI
from .routes.lottery_routes import lottery_routes
from .routes.user_routes import user_routes

app = FastAPI()

app.include_router(lottery_routes)
app.include_router(user_routes)

@app.get("/")
def read_root():
    return {"Hello": "World"}

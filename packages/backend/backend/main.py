from fastapi import FastAPI
from api.aggregates import router as aggregates
from api.users import router as users
from api.geography import router as geography
from typer import Typer
from commands.aggregator import aggregator


app = FastAPI()

app.include_router(aggregates.router)
app.include_router(users.router)
app.include_router(geography.router)
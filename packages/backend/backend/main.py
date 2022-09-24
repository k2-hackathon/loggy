from fastapi import FastAPI
from api.aggregates import router as aggregates_router
from api.users import router as users_router

app = FastAPI()

app.include_router(aggregates_router.router)
app.include_router(users_router.router)

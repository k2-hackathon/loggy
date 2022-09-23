from fastapi import FastAPI
from routers import get_stays, auth_user, create_geo_data, get_lodgings, get_user

app = FastAPI()


app.include_router(auth_user.router)
app.include_router(get_stays.router)
app.include_router(get_lodgings.router)
app.include_router(get_user.router)
app.include_router(create_geo_data.router)

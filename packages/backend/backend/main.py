from fastapi import FastAPI
from routers import auth_user_router, create_geo_data_router, get_lodgings_router, get_stays_router, get_user_router

app = FastAPI()


app.include_router(auth_user_router.router)
app.include_router(get_stays_router.router)
app.include_router(get_lodgings_router.router)
app.include_router(get_user_router.router)
app.include_router(create_geo_data_router.router)

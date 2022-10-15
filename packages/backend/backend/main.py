import api
import api_internal
from fastapi import FastAPI

app = FastAPI()

# Routing
app.include_router(api.router)
app.include_router(api_internal.router)

from fastapi import FastAPI

import api
import api_internal

app = FastAPI()

# Routing
app.include_router(api.router)
app.include_router(api_internal.router)

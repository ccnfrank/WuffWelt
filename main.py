
from fastapi import FastAPI




app = FastAPI()

from routers import berlin_routes
from routers import brandenburg_routes

app.include_router(berlin_routes)
app.include_router(brandenburg_routes)


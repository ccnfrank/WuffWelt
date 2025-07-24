
from fastapi import APIRouter

berlin_routes = APIRouter(prefix="/berlin", tags=["berlin"])
brandenburg_routes = APIRouter(prefix="/brandenburg", tags=["brandenburg"])


@berlin_routes.get("/hunds")
async def get_berlin_hunds():
    pass

@berlin_routes.get("/katze")
async def get_berlin_katze():
    pass

@brandenburg_routes.get("/hunds")
async def get_brandenburg_hund():
    pass

@brandenburg_routes.get("/katze")
async def get_brandenburg_katze():
    pass




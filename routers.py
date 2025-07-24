
from fastapi import APIRouter

berlin_routes = APIRouter(prefix="/berlin", tags=["berlin"])
brandenburg_routes = APIRouter(prefix="/brandenburg", tags=["brandenburg"])


@berlin_routes.get("/hunds")
@berlin_routes.get("/katze")

@brandenburg_routes.get("/hunds")
@brandenburg_routes.get("/katze")


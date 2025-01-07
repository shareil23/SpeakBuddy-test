from fastapi import APIRouter

check_router = APIRouter(prefix="/api/v1/check", tags=["Check API"])


@check_router.get("/health")
def check_health_v1():
    return {"status": "ok"}

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root_get():
    """root URL"""
    return {"title": "API Template", "method": "GET"}

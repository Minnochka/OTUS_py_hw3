from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/ping",
    tags=["Ping"],
)

@router.get("/",
            status_code=status.HTTP_200_OK,
            )
def get_message():
    return {
        "message": "pong",
    }
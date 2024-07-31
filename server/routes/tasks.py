from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/health")
def health_check():
    result = {"Response": "Up and running"}
    return JSONResponse(result)

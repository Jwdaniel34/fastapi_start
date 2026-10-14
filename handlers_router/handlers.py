from fastapi import APIRouter, Request, HTTPException
from starlette.responses import JSONResponse


router = APIRouter()


@router.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Oops! Something went wrong",
        },
        headers=exc.headers
    )


@router.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)
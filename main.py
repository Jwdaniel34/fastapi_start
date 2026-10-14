from fastapi import FastAPI, Request, HTTPException, status
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from book_router import router_book
from author_router import router_author
import json

app = FastAPI()

app.include_router(router_book.router)
app.include_router(router_author.router)


@app.get("/")
def read_root():
    return {"main": "Main Page"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "Oops! Something went wrong",
        },
        headers=exc.headers
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
        "This is a plain text response: " f" \n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST,
    )


@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)

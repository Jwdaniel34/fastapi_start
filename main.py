from fastapi import FastAPI
from book_router import router_book
from author_router import router_author

app = FastAPI()

app.include_router(router_book.router)
app.include_router(router_author.router)
@app.get("/")
def read_root():
    return {"hello": "world"}

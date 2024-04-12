import uvicorn

from fastapi import FastAPI
from routes import index


server = FastAPI()


PORT = 8000


@server.get("/")
async def root():
    return {"hello": "world"}


server.include_router(index.router)


if __name__ == "__main__":
    uvicorn.run("main:server", host="127.0.0.1", port=PORT, reload=True)

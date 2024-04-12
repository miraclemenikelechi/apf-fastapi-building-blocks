from fastapi import FastAPI
from routes.index import router

server = FastAPI()
server.include_router(router)


HOST = "127.0.0.1"
PORT = 8000


@server.get("/")
async def root():
    return {"hello": "world"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:server", host=HOST, port=PORT, reload=True)

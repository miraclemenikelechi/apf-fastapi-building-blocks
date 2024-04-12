from fastapi import FastAPI
from routes.index import router

server = FastAPI()


server.include_router(router)

HOST: str = "127.0.0.1"
PORT: int = 8000


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:server", host=HOST, port=PORT, reload=True)

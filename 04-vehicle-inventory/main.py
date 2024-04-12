from fastapi import FastAPI
from routes import vehicles

server = FastAPI()
server.include_router(vehicles)


HOST = "127.0.0.1"
PORT = 8000

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:server", host=HOST, port=PORT, reload=True)
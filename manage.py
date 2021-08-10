import uvicorn
from app.internal.drivers.fast_api import FastAPIServer

app = FastAPIServer.get_app()


if __name__ == "__main__":
    uvicorn.run("manage:app", host="0.0.0.0", port=8080, log_level="info")

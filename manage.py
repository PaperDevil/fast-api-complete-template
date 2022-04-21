import uvicorn
from fastapi import FastAPI

from conf.server import DEBUG, TITLE_API, DESCRIPTION_API, VERSION_API
from internal.web.api.general import general_router

app = FastAPI(
    debug=DEBUG,
    title=TITLE_API,
    description=DESCRIPTION_API,
    version=VERSION_API,
    docs_url='/swagger',
    openapi_url='/openapi.json'
)

app.include_router(general_router)

if __name__ == "__main__":
    uvicorn.run("manage:app", host="0.0.0.0", port=8080, log_level="info")

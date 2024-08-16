from fastapi import FastAPI
from app.api import endpoints
from app.config import ServerConfig

app = FastAPI()

app.include_router(endpoints.router, prefix=ServerConfig.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=ServerConfig.HOST, port=ServerConfig.PORT, reload=True, debug=True)

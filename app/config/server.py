import os

class ServerConfig:
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DOMAIN = os.getenv("DOMAIN", "http://localhost")
    API_PREFIX = "/api/v1"

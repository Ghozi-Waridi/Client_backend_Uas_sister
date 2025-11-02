import os
from typing import Dict, Any, List
from dataclasses import dataclass


## code ini menjadikan code supaya immutable
@dataclass(frozen=True)
class DatabaseConfig:
    host: str = os.getenv("DB_HOST", "localhost")
    port: int = int(os.getenv("DB_PORT", "3306"))
    name: str = os.getenv("DB_NAME", "app_db")
    user: str = os.getenv("DB_USER", "root")
    password: str = os.getenv("DB_PASSWORD", "root")
    pool_size: int = int(os.getenv("DB_POOL_SIZE", "5"))


@dataclass(frozen=True)
class ServerConfig:
    host: str = os.getenv("SERVER_HOST", "0.0.0.0")
    port: int = int(os.getenv("SERVER_HOST", "5000"))
    max_connection: int = int(os.getenv("MAX_CONNECTION", "10"))
    buffer_size: int = int(os.getenv("BUFFER_SIZE", "8192"))


@dataclass(frozen=True)
class LoggingConfig:
    level: str = os.getenv("LOG_LEVEL", "INFO")
    file: str = os.getenv("LOG_LEVEL", "logs/app.log")
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


@dataclass(frozen=True)
class ApplicationConfig:
    database: DatabaseConfig = DatabaseConfig()
    server: ServerConfig = ServerConfig()
    logging: LoggingConfig = LoggingConfig()
    allowed_origins: List[str] = None

    def __post__init__(self):
        if self.allowed_origins is None:
            origins = os.getenv(
                "ALLOWED_ORIGINS", "http://localhost:3000,http://192.168.56.1:3000"
            )
            object.__setattr__(self, "allowed_origins", origins.split(","))

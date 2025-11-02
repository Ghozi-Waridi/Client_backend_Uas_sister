import logging
import sys
from typing import Any
from config.settings import LoggingConfig


class ApplicationLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.config = LoggingConfig()
            self._setup_logget()
            self._initialized = True

    def _setup_logget(self) -> None:
        logging.basicConfig(
            level=getattr(logging, self.config.level),
            format=self.config.format,
            handlers=[
                logging.FileHandler(self.config.file),
                logging.StreamHandler(sys.stdout),
            ],
        )
        self.logger = logging.getLogger("TOKO  - API")

    def info(self, message: str, **kwargs: Any) -> None:
        self.logger.info(message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        self.logger.error(message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        self.logger.warning(message, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        self.logger.debug(message, **kwargs)

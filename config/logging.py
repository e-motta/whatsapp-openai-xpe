import logging.config

from .config import FLASK_ENV


DEV_LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

PROD_LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "level": "ERROR",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "ERROR",
    },
}

if FLASK_ENV == "development":
    logging.config.dictConfig(DEV_LOGGING_CONFIG)
else:
    logging.config.dictConfig(PROD_LOGGING_CONFIG)

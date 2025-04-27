# uvicorn app.asgi:app --host 0.0.0.0 --port 5000 --reload

import os
import dotenv
import logging
import logging.config

_ = dotenv.load_dotenv(override=True)


from app.api.router import router

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware


# Configure logging before anything else
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "%(name)s - %(levelname)s - %(message)s",
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.error": {
            "level": "WARNING",
            "handlers": ["default"],
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["default"],
            "level": "WARNING",
            "propagate": False,
        },
        "app": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False,
        }
    },
    "root": {
        "handlers": ["default"],
        "level": "WARNING",
    }
}

# Apply logging configuration
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize services on startup"""
    
    yield


# Create FastAPI application
app = FastAPI(
    title="Agentic RAG",
    version="0.1.0",
    lifespan=lifespan
)
app.add_middleware(SessionMiddleware, secret_key=os.getenv('PHI_CHAT_SECRET_KEY'))

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(router)
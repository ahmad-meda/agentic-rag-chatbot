from app.api.endpoints import rag

from fastapi import APIRouter

router = APIRouter()
router.include_router(rag.router, prefix="/rag", tags=["RAG"])
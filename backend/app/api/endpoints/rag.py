from app.core.graph import graph

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.post("/rag")
async def rag_endpoint(query: str, max_retries: int = 3):
    
    # Input to the graph
    inputs = {
        "question": query,
        "max_retries": max_retries,
        "loop_step": 0  # initial loop step
    }

    state = await graph.ainvoke(inputs)
    return state.get("generation", "No answer found.").content
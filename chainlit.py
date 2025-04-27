# chainlit.py

import chainlit as cl
from graph import graph  # your built workflow

@cl.on_chat_start
async def start_chat():
    cl.user_session.set("max_retries", 3)

@cl.on_message
async def on_message(message: cl.Message):
    question = message.content
    max_retries = cl.user_session.get("max_retries", 3)

    # Input to the graph
    inputs = {
        "question": question,
        "max_retries": max_retries,
        "loop_step": 0  # initial loop step
    }

    final_generation = None

    # Stream through the graph
    async for step in graph.astream(inputs, stream_mode="values"):
        # Extract the "generation" part if it exists
        generation = step.get("generation")
        if generation:
            final_generation = generation

    # Now display only the final generation nicely
    if final_generation:
        await cl.Message(content=final_generation.content).send()
    else:
        await cl.Message(content="Sorry, I couldn't find an answer.").send()

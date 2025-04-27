import requests
import chainlit as cl

@cl.on_chat_start
async def start_chat():
    cl.user_session.set("max_retries", 3)

@cl.on_message
async def on_message(message: cl.Message):
    response = requests.post(
        "http://127.0.0.1:5000/chat/rag",
        params={"query": message.content, "max_retries": cl.user_session.get("max_retries", 3)}
    )
    final_generation = response.json()
    if final_generation:
        await cl.Message(content=final_generation).send()
    else:
        await cl.Message(content="Sorry, I couldn't find an answer.").send()
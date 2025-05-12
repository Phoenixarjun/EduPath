import chainlit as cl
from src.llm import ask_tech, message as base_message

@cl.on_message
async def main(user_msg: cl.Message):
    chat_history = base_message.copy()

    chat_history.append({
        "role": "user",
        "parts": [{"text": user_msg.content}]
    })

    response = ask_tech(chat_history)

    chat_history.append({
        "role": "model",
        "parts": [{"text": response}]
    })

    # Send response back to Chainlit UI
    await cl.Message(content=response).send()

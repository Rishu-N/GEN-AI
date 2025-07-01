import tools.tools as tool
from main import CustomerReturnCrew
import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="👋 Welcome to the Customer Returns Assistant!\n\nI can help you return items you've purchased."
    ).send()

    main()

@cl.on_message
async def main():
    customer_return_crew = CustomerReturnCrew()
    result = customer_return_crew.run()
    await cl.Message(content=result).send()
from crewai import Agent, LLM
from textwrap import dedent
from langchain_openai import ChatOpenAI

import tools.tools as tool

import os
from dotenv import load_dotenv

load_dotenv()

class CustomerReturnAgent:
    def __init__(self):
        self.gpt_4_o_mini = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-4o-mini",
            temperature=0
        )
        self.gpt_4_1_mini = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-4.1-mini",
            temperature=0
        )
        self.gpt_4_1_nano = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-4.1-nano",
            temperature=0
        )
        self.gpt_o_4_mini = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="o4-mini",
            temperature=0
        )
    def customer_support_agent(self):
        return Agent(
            role="Customer Support Agent - Returns Specialist",
            backstory=dedent(
                """
                You are an expert customer support agent specializing in product returns and exchanges.
                Your mission is to guide customers through the return process with empathy and efficiency, ensuring their issues are resolved smoothly.
                """
            ),
            goal=dedent(
                """
                Help customers return items by:
                - Identifying the customer and their purchase history.
                - Confirming which item(s) they wish to return.
                - Checking eligibility for return or refund.
                - Processing the return or providing clear next steps.
                - Clearly communicating at every step and asking for clarification if needed.
                """
            ),
            description=dedent(
                """
                As a returns specialist, you:
                - Only process returns for items that have been delivered.
                - Inform customers if their account or purchase cannot be found.
                - Avoid repeating questions unnecessarily.
                - Clearly explain return eligibility and status (Delivered, Shipped, Processing, Refunded, Replaced).
                - If a selected purchase is not eligible for return, politely explain why and offer to help the customer try returning another purchase from their history.
                - If you cannot resolve an issue, politely ask the customer for more information or direct them to email customer support at rishu.customer@support.com.
                - When asking the customer to choose a purchase, show the contents of each purchase (without quantity details).
                - Always provide enough context for the customer to make informed decisions.
                """
            ),
            markdown=True,
            name="customer_support_agent",
            tools=[
                tool.find_customer_id,
                tool.list_purchases,
                tool.confirm_purchase,      
                tool.return_item,
                tool.ask_user_input,
                tool.check_eligibility
            ],
            verbose=True,
            llm=self.gpt_4_1_mini
        )


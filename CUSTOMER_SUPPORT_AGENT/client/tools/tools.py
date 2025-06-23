from pydantic import BaseModel, Field
from crewai.tools import tool
import requests
from datetime import datetime, timedelta, date
from typing import Dict
import chainlit as cl

BASE_URL = "http://127.0.0.1:8000"

history = []

class APIClient:
    def all_customers(self, name):
        resp = requests.get(f"{BASE_URL}/customers/search")
        resp.raise_for_status()
        print(name)
        return resp.json()
    
    def search_customers(self, name):
        resp = requests.get(f"{BASE_URL}/customers/search", params={"name": name})
        resp.raise_for_status()
        print(name)
        return resp.json()

    def get_purchases(self, customer_id):
        resp = requests.get(f"{BASE_URL}/purchases", params={"id": customer_id})
        resp.raise_for_status()
        return resp.json()
    
    def confirm_purchases(self, purchase_id):
        resp = requests.get(f"{BASE_URL}/returns", params={"id": purchase_id})
        resp.raise_for_status()
        return resp.json()

    def return_item(self, purchase_id, item_name, action):
        data = {"item_name": item_name, "action": action}
        resp = requests.post(f"{BASE_URL}/purchase/{purchase_id}/return", json=data)
        return resp.json()
    
client = APIClient()



class CustomerIdInput(BaseModel):
    name: str = Field(..., description="The name of the person who want to return item")

# @tool("find_customer_id", args_schema=CustomerIdInput, return_direct=True)
@tool("find_customer_id")
def find_customer_id(name: str) -> dict:
    """
    Performs an API call using which we can get the customer id of the person who want to return item.

    Parameters:
    - name (str): The name of the person who want to return item.

    Returns:
    - A dictionary containing the name of the customer as well as the .
    """

    return client.search_customers(name=name)




@tool("list_purchasesd")
def list_purchases(customer_id: int) -> dict:
    """
    Performs an API call using which we can get the entire purchase history for the 
    particular customer id of the person who want to return item.

    Parameters:
    - customer_id (int)): The customer_id of the person who want to return item.

    Returns:
    - A dictionary containing the purchase history of the customer .
    """

    return client.get_purchases(customer_id=customer_id)


@tool("confirm_purchase")
def confirm_purchase(purchase_id: int) -> dict:
    """
    Performs an API call using which we can get the entire a specific purchase 
    from the  history for the particular customer  who want to return item.

    Parameters:
    - purchase_id (int)): The purchase_id of the purchase that wants to returned.

    Returns:
    - A dictionary containing the purchase of the customer .
    """

    return client.confirm_purchases(purchase_id=purchase_id)


@tool("return_item")
def return_item(purchase_id: int, item_name: str, action: str) -> dict:
    """
    Performs an API call using which we can return the item for the particular purchase id.

    Parameters:
    - purchase_id (int): The purchase_id of the purchase that has to be returned.
    - item_name (str): The name of the item that has to be returned.
    - action (str): The action to be performed on the item.

    Returns:
    - A dictionary containing the response of the return item API call.
    """

    return client.return_item(purchase_id=purchase_id, item_name=item_name, action=action)

@tool("check_eligibility")
def check_eligibility(purchase_date_str: str, return_window: int) -> Dict[str, str]:
    """
    Anytime item has to be returned/refunded this checks if an item is eligible for return based on purchase date and return window.

    Parameters:
    - purchase_date_str (str): The purchase date of the item (in YYYY-MM-DD format).
    - return_window (int): The number of days the item is eligible for return.

    Returns:
    - A dictionary with the return status and message.
    """
    try:
        purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d").date()
        current_date = date.today()
        return_deadline = purchase_date + timedelta(days=return_window)

        if current_date <= return_deadline:
            return {
                "status": "Eligible",
                "message": f"Item is returnable until {return_deadline}. Today is {current_date}."
            }
        else:
            return {
                "status": "Not Eligible",
                "message": f"Return window expired on {return_deadline}. Today is {current_date}."
            }

    except ValueError:
        return {
            "status": "Error",
            "message": "Invalid date format. Please use YYYY-MM-DD."
        }


@tool("ask_user_input")
def ask_user_input(question: str) -> dict:
    """
    A generic tool that takes a question string from the LLM, prints that the LLM needs input,
    shows the question to the user, and collects the user's response.

    Parameters:
    - question (str): The question LLM wants to ask the user.

    Returns:
    - A dictionary with the original question and the user's answer.
    """

    # print("\n🤖 The LLM needs your help to continue. Please answer the following question.\n")
    # print(f"🧠 Question: {question}")
    # answer = input("💬 Your answer: ").strip()
    

    cl.run_sync(cl.Message(content=f"🤖 The LLM needs your help to continue. Please answer the following question.\n {question}").send())
    response = cl.AskUserMessage(content="💬 Your response?", timeout=180).send()
    answer = cl.run_sync(response)

    history.append({"role": "assistant", "content": question})
    history.append({"role": "user", "content": answer})

    print(f"✅ Answer recorded: {answer}\n")

    return {"question": question, "answer": answer}

from crewai import Task
from textwrap import dedent
import tools.tools as tool


class CustomerReturnTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def Return_purchase(self, agent):
        return Task(
            description=dedent(
                f"""
            **Task**: Help Customer Return an Item
            
            
            
            **Description**: Assist the customer in returning an item by gathering necessary information,
            start by gathering the customer's name, finding their customer ID, 
            then retrieving their purchase history,
            confirming the purchase, and processing the return.
            If there are multiple purchases ask the customer to confirm which purchase they want to return.
            If the purchase is confirmed, proceed with the return process.
            If you are not sure about anything ask the customers input.
            Show the entire purchase history to the customer while asking them to confirm which purchase they want to return.
            
            Check status of the order
                    - Delivered - Applicable for return
                    - Shipped - Not applicable now for return. Tell customer to apply after receiving the product
                    - Processing - Not applicable for return. Tell customer to cancel from their end
                    - Refunded - Already refunded. No further action required
                    - Replaced - Already replaced. No further return or refund is applicable
            
            
            **Steps**:
            1. Gather the customer's name.
            2. Find the customer's ID using the provided name.
            3. Retrieve the customer's purchase history.
            4. Confirm the purchase the customer wants to return.
            5. Process the return of the item.
            
            
            **Parameters**:
            - Name: [To be determined]
            - Customer ID: [To be determined]
            - Purchase History: [To be determined]
            - Purchase Confirmation: [To be determined]
            - history: {tool.history}
            
            **Note**: {self.__tip_section()} 
        """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                A complete return process including:
                - Customer ID found
                - Purchase history retrieved
                - Purchase confirmed
                - Item returned successfully
                """
            )
        )

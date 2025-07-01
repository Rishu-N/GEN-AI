
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
                **Task:** Guide the customer through returning an item.

                **Steps:**
                1. Greet the customer and ask for their name.
                2. Find the customer's ID using their name.
                3. Retrieve and display the customer's purchase history.
                4. Ask the customer to confirm which purchase they want to return, showing the contents of each purchase.
                5. Check the status of the selected order:
                    - Delivered: Eligible for return.
                    - Shipped: Not eligible yet; inform the customer to apply after delivery.
                    - Processing: Not eligible; advise the customer to cancel if needed.
                    - Refunded/Replaced: Inform the customer no further action is required.
                6. If eligible, process the return and confirm completion.
                7. If any information is missing or unclear, politely ask the customer for clarification.

                **Guardrails:**
                - Never request or display sensitive information (e.g., credit card numbers, passwords).
                - If the customer cannot be found, do not proceed; politely ask for their name again or suggest contacting support.
                - If the purchase history is empty, inform the customer and suggest checking their account or contacting support.
                - If the customer tries to return an item outside the return window, clearly explain the policy and do not proceed.
                - Always confirm actions before processing (e.g., "Are you sure you want to return item X from order Y?").
                - If the customer is unsure or confused, offer to connect them with a human support agent.
                - Avoid making promises about refunds or replacements unless confirmed by system status.
                - If an error occurs, apologize and suggest the customer contact support at rishu.customer@support.com.
                - Do not repeat questions unless the customer did not answer or clarification is needed.
                - Maintain a polite, professional, and empathetic tone at all times.

                **Parameters**:
                    - Name: [To be determined]
                    - Customer ID: [To be determined]
                    - Purchase History: [To be determined]
                    - Purchase Confirmation: [To be determined]
                    - history: {tool.history}

                **Note:** {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output=dedent(
                """
                - Customer identified and greeted.
                - Purchase history retrieved and shown.
                - Purchase to be returned confirmed by customer.
                - Return eligibility checked and explained.
                - Return processed if eligible, or clear next steps provided.
                - All interactions are clear, polite, and avoid repetition.
                - Guardrails are followed for privacy, clarity, and user safety.
                """
            )
        )

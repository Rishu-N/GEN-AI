from crewai import Crew,Process
from textwrap import dedent
import tools.tools as tool  
from agents import CustomerReturnAgent
from tasks import CustomerReturnTasks
from crewai.project import CrewBase
from dotenv import load_dotenv
import os
import logging


logging.getLogger().setLevel(logging.CRITICAL)


load_dotenv()
os.environ["CREWAI_TELEMETRY_ENABLED"] = "false"


@CrewBase
class CustomerReturnCrew:
    # def __init__(self,):
        # self.name = name

    def run(self):

        agents = CustomerReturnAgent()
        tasks = CustomerReturnTasks()

        customer_agent = agents.customer_support_agent()
        customer_task = tasks.Return_purchase(customer_agent)

        crew = Crew(
            agents=[customer_agent],
            tasks=[customer_task],
            verbose=True,
            # memory=True,
            tools=CustomerReturnAgent().customer_support_agent().tools,
            chat_llm=CustomerReturnAgent().customer_support_agent().llm,
            process=Process.sequential,
            history=True,
        
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to Return Customer Crew ##")
    print('-------------------------------')
    
    # name = "alice"
    name = input(
        dedent("""
      Please give us your name so we can assist you with your return request.
    """))
    tool.history.append({"role": "assistant", "content":"Please give us your name so we can assist you with your return request."})
    tool.history.append({"role": "user", "content": {name}})
    customer_return_crew = CustomerReturnCrew(name)
    result = customer_return_crew.run()
    print(result)
    


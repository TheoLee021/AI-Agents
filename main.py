import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, crew, agent, task

@CrewBase
class TranslatorCrew:
    
    @agent
    def translator_agent(self):
        return Agent(
            config=self.agents_config["translator_agent"],
        )
    
    @task
    def translate_task(self):
        return Task(
            config=self.tasks_config["translate_task"],
        )
    
    @task
    def retranslate_task(self):
        return Task(
            config=self.tasks_config["retranslate_task"],
        )
    
    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
    
TranslatorCrew().assemble_crew().kickoff(inputs={"sentence": "I'm Theo and I like to ride my bike in San Diego"})
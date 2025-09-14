from crewai import Agent,Task, Crew
from crewai.project import CrewBase, crew, task, agent
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class LinkedinMarketing():

    # Importing the config files #

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher_agent"], # type: ignore[index]
            verbose=True
        )

    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["writer_agent"], # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"], # type: ignore[index]
            agent=self.researcher_agent()
        )

    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config["writer_task"], # type: ignore[index]
            agent=self.writer_agent()
        )

    @crew
    def linkedinMarketingCrew(self) -> Crew:
        return Crew(
            agents=[self.researcher_agent(), self.writer_agent()],
            tasks=[self.research_task(), self.writer_task()],
            verbose=True
        )

if __name__ == "__main__":
    linkedin_marketing = LinkedinMarketing()
    linkedin_marketing.linkedinMarketingCrew().kickoff(inputs={"topic":"Agentic Ai"})
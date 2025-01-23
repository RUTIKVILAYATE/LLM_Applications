from crewai import Crew, Process 
from agents import blog_researcher_agent,blog_writer_agent
from tasks import research_task,write_task


# from dotenv import load_dotenv

# load_dotenv()



# Forming the text focused-crew with some enhanced configuration

crew = Crew(
    agents = [blog_researcher_agent,blog_writer_agent],
    tasks = [research_task , write_task]
    process = Process.sequential,   # Optional -> Sequential execution task is default 
    memory = True,
    caceh = True,
    max_rpm = 100,
    share_crew = True
)


# start the task exection process with enhanced feedback 

result = crew.kickoff(inputs={'topic': "AI VS ML VS DL VS DATA SCIENCE"})
print(result)
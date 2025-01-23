from crewai import Agent
from tools import yt_tool


from dotenv import load_dotenv
load_dotenv()


import os 
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview" 


# Create a Senior Blog Content Researcher

blog_researcher_agent = Agent(
    role = "Blog Researcher from Youtube Videos"
    goal = "get the relevant videos content from the topic{topic} from Youtube channel",
    verboe = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science, Machine Learning and GenAI and Providing Suggestions"

    
    )
    tools = [yt_tool], 
    llm = llm,
    allow_delegation = True     # if set true -> task done by this agent can be transferable to someone else

)


#  Creating a Senior Blog Writer Agent with Youtube Tool

blog_writer_agent= Agent(
    role = "Blog Writer"
    goal = "Narrate compelling text stories about the video{topic} from Youtube channel",
    verboe = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivates and educate, bringing new"
        "bringing new discoveries to light in an accessible manner"

    
    ),
    tools = [yt_tool], 
    llm = llm,
    allow_delegation = False



) 
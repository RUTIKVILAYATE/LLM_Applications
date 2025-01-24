import os 
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

# call the gemini models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose = True,
                             temperature = 0.5,
                             google_api_key = os.getenv("GOOGLE_API_KEY"))


# creating a senior researcher agent with memory and verbose mode 


news_researcher = Agent(
    role = "Senior Researcher",
    goal = "Uncover ground breaking technologies in {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to express and share knowledge that could change"
        "the world"  
    ),
    tools=[tool],
    llm = llm,
    allow_delegation = True
)


news_writer = Agent(
    role = "Writer",
    goal = "Narrate compelling text stories about {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"  
    ),
    tools=[tool],
    llm = llm,
    allow_delegation = False
)
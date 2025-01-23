from crewai import Task
from tools import yt_tool
from agents import blog_researcher_agent,blog_writer_agent


# Research Task 
research_task = Task(
    description = ( "Identify the video {topic}",
                   "Get detailed information about the video from the channel"

),
expected_output = 'A comprehensive 3 paragraph long report based on the {topic} of the video content'
tools = [yt_tool],
agent = blog_researcher_agent
)


# Writing task with language model configuration

write_task  = Task(
    description=(
        "get the info from the youtube channel on the topic {topic}"
    ),
    expected_output = "Summarize the info from the youtube channel video from the topic{topic} and create the content from the blog",
    tools=[yt_tool],
    agent = blog_writer_agent,
    async_execution = False,     # if set to True -> agents will work parallely instead of sequence
    output_file = "new-blog-post.md"    # example of output customization
)
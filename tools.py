from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

print(search_tool.run(search_query="Korea war"))

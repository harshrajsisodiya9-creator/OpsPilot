from langgraph.prebuilt import ToolNode

from tools import create_tasks, get_task_from_db

tasks_tools = ToolNode([get_task_from_db, create_tasks])

from langchain_core.tools import tool

from db.database import create_tasks_in_db, get_tasks


@tool
def get_task_from_db():
    """Get all tasks from db"""

    return get_tasks()


@tool
def create_tasks(title, status: str = "pending"):
    """create and insert new tasks into the db"""

    return create_tasks_in_db(title=title, status=status)

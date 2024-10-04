from module_17_tasks_17_2.app.models.task import Task
from module_17_tasks_17_2.app.models.user import User

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
from includes import *


class AddTask(BaseModel):
    title: str
    description: str = ""
    due_date: datetime.datetime


class AddTaskRedis(BaseModel):
    id: int
    title: str
    description: str = ""
    due_date: datetime.datetime


class ChangeTask(BaseModel):
    task_id: int
    change_field: str
    content: Union[str, datetime.datetime]


class DeleteTask(BaseModel):
    task_id: int

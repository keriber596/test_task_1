import database
import models
import schemes
from includes import *
import redis_services


def create_database():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_task(task: schemes.AddTask, db: orm.Session):
    new_task = models.Task(title=task.title, description=task.description, due_date=task.due_date)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    task_redis = schemes.AddTaskRedis(title=task.title, description=task.description, due_date=task.due_date, id=new_task.id)
    redis_services.add_data(task_redis)
    return {"msg": f"task #{new_task.id} - {task.title}: {task.description} added"}


def change_task(task: schemes.ChangeTask, db: orm.Session):
    onchange_task = db.query(models.Task).get(task.task_id)
    if onchange_task:
        setattr(onchange_task, task.change_field, task.content)
        db.commit()
        if task.change_field == 'status' and task.content == 'done':
            message_url = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendMessage"
            data = {'chat_id':os.environ.get("CHAT_ID"), 'text':f"task #{task.task_id} - {onchange_task.title} is done "}
            requests.post(message_url, data=data)
        return {"msg": f"task #{task.task_id} changed"}
    else:
        return {"msg": "no task with the following id"}


def delete_task(task: schemes.DeleteTask, db: orm.Session):
    ondelete_task = db.query(models.Task).get(task.task_id)
    if ondelete_task:
        db.delete(ondelete_task)
        db.commit()
        return {"msg": f"task #{task.task_id} deleted"}
    else:
        return {"msg": "no task with the following id"}


def get_task(task_id: int, db: orm.Session):
    task = db.query(models.Task).get(task_id)
    return task

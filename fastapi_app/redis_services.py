from includes import *
import schemes

r = redis.Redis(host=os.environ.get("REDIS_HOST"), port=int(os.environ.get("REDIS_PORT")), db=0)


def add_data(task: schemes.AddTaskRedis):
    data = {"msg":f"task #{task.id} - {task.title} : {task.description} was added till {task.due_date}"}
    r.xadd(name=os.environ.get("STREAM_NAME"), fields=data)

import fastapi

import schemes
import services
from includes import *
app = FastAPI(docs_url='/docs', openapi_url='/openapi.json')

services.create_database()


@app.post("/task/add")
def add_task(task: schemes.AddTask, db: orm.Session = fastapi.Depends(services.get_db)):
    return services.add_task(task, db)


@app.post("/task/edit")
def change_task(task: schemes.ChangeTask, db: orm.Session = fastapi.Depends(services.get_db)):
    return services.change_task(task, db)


@app.get("/task/get")
def get_task(task_id: int, db: orm.Session = fastapi.Depends(services.get_db)):
    return services.get_task(task_id, db)


@app.delete("/task/delete")
def delete_task(task: schemes.DeleteTask, db: orm.Session = fastapi.Depends(services.get_db)):
    return services.delete_task(task, db)


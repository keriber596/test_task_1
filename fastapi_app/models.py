from includes import *
import database


class Task(database.Base):
    __tablename__ = "tasks"
    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String, default="")
    description = sql.Column(sql.String, default="")
    due_date = sql.Column(sql.DateTime, default=datetime.datetime.now())
    status = sql.Column(sql.String, default="pending") #pending, in_process, done

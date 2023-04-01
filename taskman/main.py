# -*- coding: utf-8 -*-
from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TaskRequest(BaseModel):
    name: str
    description: str


class Task(TaskRequest):
    item_id: int


tasks: Dict[str, Task] = {}

@app.get('/')
def home():
    return {"message":"home"}
  

@app.get('/tasks')
def get_tasks() -> List[Task]:
    return list(tasks.values())


@app.get('/tasks/{item_id}')
def get_tasks(item_id: str) -> Task:
    return tasks[item_id]


@app.put('/tasks/{item_id}')
def update_item(item_id: str, item: TaskRequest) -> None:
    tasks[item_id] = Task(
        item_id=item_id,
        name=item.name,
        description=item.description,
    )


@app.post('/tasks')
def create_item(item: TaskRequest):
    item_id = str(len(tasks) + 1)
    tasks[item_id] = Task(
        item_id=item_id,
        name=item.name,
        description=item.description,
    )

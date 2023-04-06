# -*- coding: utf-8 -*-
from typing import Dict, List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
    html_content = """ <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>hs-heilbronn-devsecops-tigers</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get('/tasks')
def get_tasks() -> List[Task]:
    return list(tasks.values())


@app.get('/tasks/{item_id}')
def get_task(item_id: str) -> Task:
    return tasks[item_id]


@app.put('/tasks/{item_id}')
def update_task(item_id: str, item: TaskRequest) -> None:
    tasks[item_id] = Task(
        item_id=item_id,
        name=item.name,
        description=item.description,
    )


@app.post('/tasks')
def create_task(item: TaskRequest):
    item_id = str(len(tasks) + 1)
    tasks[item_id] = Task(
        item_id=item_id,
        name=item.name,
        description=item.description,
    )


def delete_tasks():
    tasks.clear()

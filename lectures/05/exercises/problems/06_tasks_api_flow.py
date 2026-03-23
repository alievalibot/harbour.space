"""Problem 06: POST -> GET tasks flow.

Task:
1. Keep in-memory task storage (dict or list)
2. Implement POST /tasks to add task with generated id
3. Implement GET /tasks to return all tasks
4. Verify: after POST, GET returns added task

Optional:
- Add GET /tasks/{task_id} with 404 for missing task
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class TaskIn(BaseModel):
    # TODO: add fields
    pass
    title: str
    completed: bool = False  

class TaskOut(BaseModel):
    # TODO: add id + task fields
    pass


# TODO: create in-memory storage and next_id counter
    id: int
    title: str
    completed: bool


storage: dict[int, TaskOut] = {}
next_id: int = 1


@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskIn) -> TaskOut:
    global next_id
    task = TaskOut(id=next_id, title=payload.title, completed=payload.completed)
    storage[next_id] = task
    next_id += 1
    return task

    # TODO: create/store/return task
    raise NotImplementedError


@app.get("/tasks", response_model=list[TaskOut])
def get_tasks() -> list[TaskOut]:
    return list(storage.values())

    # TODO: return all tasks
    raise NotImplementedError

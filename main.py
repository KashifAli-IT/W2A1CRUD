from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for tasks
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "title": "Build CRUD API",
        "completed": False
    },
    {
        "id": 3,
        "title": "Push Project to GitHub",
        "completed": False
    }
]

# Request body for creating a new task
class TaskCreate(BaseModel):
    title: str
    completed: bool = False
# Request body for updating an existing task
class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None 

@app.put("/tasks/{id}")
def update_task(id: int, task_update: TaskUpdate):
    # Find the task with the given ID
    for task in tasks:
        if task["id"] == id:
            # Empty body
            if task_update.title is None and task_update.completed is None:
                return JSONResponce(
                    status_code=400,
                    content={
                        "error": "Request body cannot be empty"
                    }
                )
            # Update title if provided
            if task_update.title is not None:
                if not task_update.title.strip():
                    return JSONResponse(
                        status_code=400,
                        content={
                            "error": "Title cannot be empty"
                        }
                    )
                task["title"] = task_update.title.strip()
            # Update completed status if provided
            if task_update.completed is not None:
                task["completed"] = task_update.completed

            return task
    # Task not found
    return JSONResponse(
        status_code=404,
        content={
            "error": f"Task with ID {id} not found"
        }
    )   

@app.delete("/tasks/{id}", status_code=204)    
def delete_task(id: int):
    for index, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(index)
            return Response(status_code=204)
    
    return JSONResponse(
        status_code=404,
        content={
            "error": f"Task with ID {id} not found"
        }
    )
    
@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0", 
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def read_health():
    return {
        "status": "ok"
        }

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
   
    return JSONResponse(
        status_code=404,
        content={
            "error": f"Task with ID {id} not found"
            }
        )        

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # Validate title
    if not task.title.strip():
        return JSONResponse(
            status_code=400,
            content={
                "error": "Title cannot be empty"
            }
        )
    
    # Generate a new ID for the task
    new_id = max(existing_task["id"] for existing_task in tasks) + 1 if tasks else 1
    
    # Create a new task 
    new_task = {
        "id": new_id,
        "title": task.title.strip(),
        "completed": task.completed
    }

    # Add the new task to the in-memory storage
    tasks.append(new_task)      

    return new_task
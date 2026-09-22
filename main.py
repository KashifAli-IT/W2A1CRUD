from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
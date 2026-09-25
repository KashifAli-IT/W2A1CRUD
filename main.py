from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel
from database import init_db

app = FastAPI()
init_db()

# In-memory storage for tasks
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build CRUD API",
        "done": False
    },
    {
        "id": 3,
        "title": "Push Project to GitHub",
        "done": False
    }
]

# Request body for creating a new task
class TaskCreate(BaseModel):
    title: str
    done: bool = False
# Request body for updating an existing task
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None 

@app.put("/tasks/{id}", description="Update an existing task by ID")
def update_task(id: int, task_update: TaskUpdate):
    # Find the task with the given ID
    for task in tasks:
        if task["id"] == id:
            # Empty body
            if task_update.title is None and task_update.done is None:
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
            # Update done status if provided
            if task_update.done is not None:
                task["done"] = task_update.done

            return task
    # Task not found
    return JSONResponse(
        status_code=404,
        content={
            "error": f"Task with ID {id} not found"
        }
    )   

@app.delete("/tasks/{id}", status_code=204, description="Delete a task by ID")    
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

@app.get("/", description="Root endpoint that provides basic information about the API")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0", 
        "endpoints": ["/tasks"]
    }

@app.get("/health", description="Health check endpoint to verify the API is running")
def read_health():
    return {
        "status": "ok"
        }

@app.get("/tasks", description="Get all tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}", description="Get a specific task by ID")
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

@app.post("/tasks", status_code=201, description="Create a new task")
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
        "done": task.done
    }

    # Add the new task to the in-memory storage
    tasks.append(new_task)      

    return new_task
from fastapi import FastAPI
from fastapi.responses import JSONResponse

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
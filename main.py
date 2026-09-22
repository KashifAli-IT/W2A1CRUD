from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hi there!": "Welcome to the FastAPI application."}
# Task API

A simple RESTful CRUD API built with **FastAPI** as part of the FlyRank AI Backend Engineer internship task.

The API manages tasks with three fields:

* `id` — unique task ID
* `title` — task title
* `done` — completion status

The project uses an in-memory Python list as its temporary data store.

## Features

* Create tasks
* List all tasks
* Get a single task
* Update a task
* Delete a task
* Input validation
* Proper HTTP status codes
* Interactive Swagger UI documentation

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* REST API
* Swagger UI / OpenAPI

## Installation & Run

Clone the repository:

```bash
git clone https://github.com/KashifAli-IT/W2A1CRUD.git
cd W2A1CRUD
```

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the API:

```powershell
uvicorn main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

## Swagger UI

Interactive API documentation is available at:

```text
http://localhost:8000/docs
```

![Swagger UI](docs/swagger-ui.png)

## API Endpoints

| Method | Endpoint      | Description             | Success |
| ------ | ------------- | ----------------------- | ------- |
| GET    | `/`           | Returns API information | 200     |
| GET    | `/health`     | Checks API health       | 200     |
| GET    | `/tasks`      | Returns all tasks       | 200     |
| GET    | `/tasks/{id}` | Returns one task        | 200     |
| POST   | `/tasks`      | Creates a new task      | 201     |
| PUT    | `/tasks/{id}` | Updates a task          | 200     |
| DELETE | `/tasks/{id}` | Deletes a task          | 204     |

### Error Responses

| Status | Meaning                     |
| ------ | --------------------------- |
| 400    | Invalid or empty request    |
| 404    | Task not found              |
| 422    | Invalid request format/type |

## Example

Create a task:

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{\"title\":\"Buy milk\"}"
```

Example response:

```text
HTTP/1.1 201 Created
content-type: application/json

{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

## CRUD Flow

```text
POST   /tasks       → Create
GET    /tasks       → Read all
GET    /tasks/{id}  → Read one
PUT    /tasks/{id}  → Update
DELETE /tasks/{id}  → Delete
```

## Project Structure

```text
W2A1CRUD/
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
└── docs/
    └── swagger-ui.png
```

## Note

This project currently uses an in-memory list instead of a persistent database. Data resets whenever the server restarts.

## Author

**Kashif Ali**

GitHub: [KashifAli-IT](https://github.com/KashifAli-IT)

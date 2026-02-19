# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple web service using the FastAPI framework. This assignment introduces students to RESTful concepts, route definitions, and automatic API documentation.

## 📝 Tasks

### 🛠️ Project Setup and Dependencies

#### Description
Create a new Python project and install `fastapi` and `uvicorn`. Prepare a starter file to launch the application.

#### Requirements
Completed program should:

- Include a `requirements.txt` or list of dependencies mentioning `fastapi` and `uvicorn`.
- Provide a Python script (e.g. `main.py`) that imports FastAPI and creates an application instance.
- Add instructions or comments explaining how to start the server using `uvicorn`.

### 🛠️ Define Basic Endpoints

#### Description
Implement several routes to handle HTTP requests and return JSON responses.

#### Requirements
Completed program should:

- Define at least one GET endpoint (`/items/`) that returns a list of items.
- Define a GET endpoint with a path parameter (e.g. `/items/{item_id}`) that returns a specific item.
- Include a POST endpoint to add a new item to the list. The request body should be validated using Pydantic models.
- Responses must be JSON serializable and use appropriate status codes.

### 🛠️ Data Models and Validation

#### Description
Use Pydantic models to define the shape of data sent to and from the API.

#### Requirements
Completed program should:

- Create Pydantic `BaseModel` classes for request and response bodies (e.g. `Item`, `ItemCreate`).
- Validate incoming POST data automatically; invalid requests should return a 422 error.
- Document the models using inline comments or docstrings.

### 🛠️ Optional Enhancements

#### Description
Add further features or polish the API to make it more realistic or user-friendly.

#### Requirements
Completed program could:

- Implement PUT and DELETE endpoints to allow full CRUD operation on the item list.
- Use an in-memory Python list or dictionary to store items and simulate a database.
- Add query parameters for filtering or pagination.
- Demonstrate how to view the automatic Swagger UI (`/docs`) or Redoc documentation (`/redoc`).
- Include a simple Bash script or instructions for testing with `curl` or `http` commands.

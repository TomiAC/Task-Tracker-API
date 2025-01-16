# Flask Tasks API

This project is an API developed in Flask to manage tasks. It allows you to create, read, update, and delete tasks stored in a JSON file.

## Features

- **GET /tasks**: Retrieves a list of tasks, with an option to filter by status.
- **POST /task**: Adds a new task.
- **PUT /task/<task_id>**: Updates the status of an existing task.
- **DELETE /task/<task_id>**: Deletes a specific task.

## Requirements

- Python 3.10+
- Flask
- pytest (for testing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/flask-tasks-api.git
   cd flask-tasks-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `tasks.json` file with the following initial content:
   ```json
   []
   ```

## Usage

1. Run the application:
   ```bash
   flask run
   ```

2. The API will be available at `http://127.0.0.1:5000`.

## Endpoints

### GET /tasks
Retrieve all tasks or filter by status.

- **Headers:**
  - `Content-Type: application/json`
- **Body (optional):**
  ```json
  {
    "status": "status_to_filter"
  }

### POST /task
Add a new task.

- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
    "description": "Task description"
  }

### PUT /task/<task_id>
Update the status of an existing task.

- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
    "status": "new_status"
  }

### DELETE /task/<task_id>
Delete a specific task.

## Tests

Run tests using `pytest`:

```bash
pytest test_flask_api.py
```

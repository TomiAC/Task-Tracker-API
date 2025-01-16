import pytest
import json
from app import app  # Asegúrate de que el archivo de tu aplicación se llame app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Configurar un archivo de tareas temporal para pruebas
    with open('tasks_test.json', 'w') as file:
        json.dump([
            {
                "id": 1,
                "description": "Sample Task",
                "status": "pending",
                "created_at": "2025-01-01 10:00:00",
                "updated_at": "2025-01-01 10:00:00"
            }
        ], file, indent=4)

    yield client

    # Limpiar archivo temporal después de las pruebas
    with open('tasks_test.json', 'w') as file:
        json.dump([], file, indent=4)

def test_get_tasks(client):
    # Caso: Obtener todas las tareas
    response = client.get('/tasks')
    assert response.status_code == 200
    tasks = response.get_json()
    assert len(tasks) == 1
    assert tasks[0]['description'] == "Sample Task"

    # Caso: Obtener tareas con un estado específico
    response = client.get('/tasks', headers={'Content-Type': 'application/json'}, json={"status": "pending"})
    assert response.status_code == 200
    tasks = response.get_json()
    assert len(tasks) == 1
    assert tasks[0]['status'] == "pending"

def test_add_task(client):
    # Caso: Agregar una nueva tarea
    response = client.post('/task', headers={'Content-Type': 'application/json'}, json={"description": "New Task"})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Task added successfully!'

    # Verificar que la tarea se agregó
    with open('tasks_test.json', 'r') as file:
        tasks = json.load(file)
    assert len(tasks) == 2
    assert tasks[1]['description'] == "New Task"

def test_update_task(client):
    # Caso: Actualizar una tarea existente
    response = client.put('/task/1', headers={'Content-Type': 'application/json'}, json={"status": "completed"})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Task updated successfully!'

    # Verificar que la tarea fue actualizada
    with open('tasks_test.json', 'r') as file:
        tasks = json.load(file)
    assert tasks[0]['status'] == "completed"

def test_delete_task(client):
    # Caso: Eliminar una tarea existente
    response = client.delete('/task/1', headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Task deleted successfully!'

    # Verificar que la tarea fue eliminada
    with open('tasks_test.json', 'r') as file:
        tasks = json.load(file)
    assert len(tasks) == 0
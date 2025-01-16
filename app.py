from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def index():

    status = None

    if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
        if(request.json['status']):
            status = request.json['status']

    with open ('tasks.json', 'r') as file:
        tasks = json.load(file)

    if status:
        tasks = [task for task in tasks if task['status'] == status]

    return jsonify(tasks), 200

@app.route('/task', methods=['POST'])
def add_task():
    task_description = request.json['description']

    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    highest_index = 0
    for dic in tasks:
        for key, value in dic.items():
            if(key=='id'):
                highest_index = value

    tasks.append(
        {
            'id': highest_index+1, 
            'description': task_description, 
            'status': 'Null', 
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    )

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

    return jsonify({'message': 'Task added successfully!'}), 200

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task_status = request.json['status']

    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    for dic in tasks:
        for key, value in dic.items():
            if(key=='id' and value==task_id):
                dic['status'] = new_task_status
                dic['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

    return jsonify({'message': 'Task updated successfully!'}), 200

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):

    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    for dic in tasks:
        for key, values in dic.items():
            if(key=='id' and values==task_id):
                tasks.remove(dic)
    
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    
    return jsonify({'message': 'Task deleted successfully!'}), 200
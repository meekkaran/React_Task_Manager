from flask import Flask,jsonify,request
from prisma import PrismaClient

app = Flask(__name__)
prisma = PrismaClient()

#Create a task
@app.route('/tasks', methods=['GET'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    status=data.get('status')
    task = prisma.task.create(
        {
        "data": {
            "title": title,
            "status": status
        }
        }
    )
    return jsonify(task)

#Update Task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    status=data.get('status')
    task = prisma.task.update(
        {
            "where": {
                "id": task_id
            },
            "data": {
                "title" : title,
                "status" : status
            }
        }
    )
    return jsonify(task)


#Delete Task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_taks(task_id):
    task = prisma.task.delete(
        {
            "where": {
                "id": task_id
            }
        }
    )
    return jsonify(task)

if __name__ == '__main__':
    app.run()


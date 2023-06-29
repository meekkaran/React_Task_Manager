from flask import Flask,jsonify, request
from prisma import PrismaClient

app = Flask(__name__)
prisma = PrismaClient()

#Create a task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    status = data.get('status')

    if not title or not status:
        return jsonify({'error': 'Title and status are required'}), 400
    
    try:
        task  = prisma.task.create(
            {
                'data': {
                    "title": title,
                    "status": status
                }
            }
        )
        return jsonify(task)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

#Update Task
@app.route('/tasks/<int:task_id>', methods=['PUT'])    
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    status = data.get('status')

    if not title or not status:
        return jsonify({'error': 'Title and status are required'}),400
    try:
        task = prisma.task.update(
            {
                "where": {
                    "id": task_id,
                },
                "data": {
                    "title": title,
                    "status": status
                }
            }
        )
        return jsonify(task)
    except Exception as e:
        return jsonify({'error':str(e)}), 500

#Delete Task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = prisma.task.delete(
            {
                "where":{
                    "id":task_id
                }
            }
        )
        return jsonify(task)
    except Exception as e:
        return jsonify({'error', str(e)}), 500
    
if __name__ == '__main__':
    app.run()
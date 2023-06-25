from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message':'hello world'})#this is a simple GET request

@app.route('/greeting', methods=['POST'])#expects a JSON payload containing field called 'name'
def greeting():
    name = request.json.get('name')
    if name:
        return jsonify({'message': f'Hello, (name)!'})
    else:
        return  jsonify({'error':"Invalid request. Please provide a name"}), 400

if __name__ =='__main__':
    app.run()
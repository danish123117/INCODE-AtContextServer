from flask import Flask, jsonify
import json

app = Flask(__name__)

# Function to load JSON data from file
def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Route to serve test1.json
@app.route('/test1.json', methods=['GET'])
def get_test1():
    data = load_json('test1.json')
    return jsonify(data)

# Route to serve test2.json
@app.route('/test2.json', methods=['GET'])
def get_test2():
    data = load_json('test2.json')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

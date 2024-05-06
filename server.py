from flask import Flask, jsonify
import json
from waitress import serve
app = Flask(__name__)

# Function to load JSON data from file
def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Route to serve eng 1000.json
@app.route('/emg1000.jsonld', methods=['GET'])
def get_test1():
    data = load_json('emg1000.jsonld')
    return jsonify(data)

# Route to serve emgfeatures.json
@app.route('/emgFeatures.jsonld', methods=['GET'])
def get_test2():
    data = load_json('emgFeatures.jsonld')
    return jsonify(data)

@app.route('/polarACC.jsonld', methods=['GET'])
def get_test3():
    data = load_json('polarACC.jsonld')
    return jsonify(data)

@app.route('/polarECG.jsonld', methods=['GET'])
def get_test4():
    data = load_json('polarECG.jsonld')
    return jsonify(data)

@app.route('/polarHR.jsonld', methods=['GET'])
def get_test5():
    data = load_json('polarHR.jsonld')
    return jsonify(data)

if __name__ == '__main__':
    serve(app, host= "0.0.0.0", port= 5051)

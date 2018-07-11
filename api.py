import flask
import flask_restful
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


@app.route("/query-sample", methods=['GET'])
def query_sample():
    return 'Todo..'


@app.route("/json-example", methods=['POST'])
def json_example():
    req_data = request.get_json()
    arr = [req_data['name'],req_data['age'],req_data['profession']]
    print arr
    return 'todo'


if __name__ == '__main__':
    app.run(debug=True, port=5000)


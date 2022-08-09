import json
from flask import Flask, request, Response
from dbconn import engine
from sqlalchemy.orm import Session
from models import student, progress
import service


app = Flask(__name__)


@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    status = service.get_single_record(id)
    return status


@app.route('/student', methods=['GET'])
def get_students():
    status = service.get_all_records()
    return status


@app.route('/student', methods=['POST'])
def create():
    req_data = json.loads(request.data)
    status = service.create_record(req_data)
    return status


@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
    status = service.delete_single_record(id)
    return status


@app.route('/student', methods=['DELETE'])
def delete_students():
    status = service.delete_all_records()
    return status


if __name__ == "__main__":

    app.run(debug=True, port=5000)

import json
from flask import Flask, request, Response
from dbconn import engine
from sqlalchemy.orm import Session
from models import student, progress
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import delete


app = Flask(__name__)


@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    with Session(engine) as session:
        row = session.query(student).filter_by(id=id).first()
        if row != None:
            return dict(row)
        else:
            return Response(status=404)


@app.route('/student', methods=['GET'])
def get_students():
    with Session(engine) as session:
        rows = session.query(student).all()
        return [dict(row) for row in rows]


@app.route('/student', methods=['POST'])
def create():
    req_data = json.loads(request.data)
    if not isinstance(req_data, list):
        student_datas = [req_data]
    else:
        student_datas = req_data
    with Session(engine) as session:
        for data in student_datas:
            Base = automap_base()
            Base.prepare(autoload_with=engine)
            Student = Base.classes.student
            student_data = {key: value for key,
                            value in data.items() if key in student.columns.keys()}
            progress_data = {key: value for key, value in data.items(
            ) if key in progress.columns.keys()}
            Progress = Base.classes.progress
            st1 = Student(**student_data)
            session.add(st1)
            session.commit()
            prog1 = Progress(student_id=st1.id, **progress_data)
            session.add(prog1)
            session.commit()
    return Response(status=201)


@app.route('/student/<id>', methods=['DELETE'])
def delete_student(id):
    with Session(engine) as session:
        Base = automap_base()
        Base.prepare(autoload_with=engine)
        Student = Base.classes.student
        record = session.query(student).filter(Student.id==id)
        result = session.execute(session.query(record.exists())).scalar()
        if result == False:
            return Response(status=404)
        session.execute(delete(student).where(student.c.id == id))
        session.commit()
    return Response(status=204)


@app.route('/student', methods=['DELETE'])
def delete_students():
    with Session(engine) as session:
        session.query(student).delete()
        session.commit()
    return Response(status=204)


if __name__ == "__main__":

    app.run(debug=True, port=5000)

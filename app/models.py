from sqlalchemy import ForeignKey, MetaData
from sqlalchemy.schema import Table, Column
from sqlalchemy.types import Integer, String, VARCHAR

metadata_obj = MetaData()

student = Table('student', metadata_obj,
                Column('id', Integer, primary_key=True),
                Column('name', VARCHAR(50), nullable=False),
                Column('age', Integer, nullable=False),
                Column('class', VARCHAR(50), nullable=False),
                Column('mother_name', VARCHAR(50), nullable=False),
                Column('father_name', VARCHAR(50), nullable=False),
                Column('mother_occupation', VARCHAR(50), nullable=True),
                Column('father_occupation', VARCHAR(50), nullable=True),
                Column('address', String(150), nullable=False),
                Column('phone-number-1', String(10), nullable=False),
                Column('phone-number-2', String(10), nullable=True),
                Column('email', VARCHAR(50), nullable=True),
                )

progress = Table('progress', metadata_obj,
                 Column('id', Integer, primary_key=True),
                 Column('student_id', Integer, ForeignKey(
                     "student.id", ondelete='CASCADE'), nullable=False),
                 Column('exam_name', VARCHAR(50), nullable=False),
                 Column('grade', VARCHAR(2)),
                 Column('physics', Integer, nullable=False),
                 Column('chemistry', Integer, nullable=False),
                 Column('maths', Integer, nullable=False),
                 Column('total', Integer, nullable=False),
                 Column('percentage', Integer, nullable=False),
                 )

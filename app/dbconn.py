from sqlalchemy import create_engine
from models import metadata_obj
from sqlalchemy.orm import Session

username = 'py-user'
password = 'Py-pass1234'

engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost/project1", future=True)

metadata_obj.bind = engine

metadata_obj.create_all()
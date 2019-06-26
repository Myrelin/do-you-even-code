import os
from modules import process_timer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

user_name = os.environ.get('PSQL_USER_NAME')
password = os.environ.get('PSQL_PASSWORD')
host = os.environ.get('PSQL_HOST')
database_name = os.environ.get('PSQL_DB_NAME')

engine = create_engine('postgresql://' + user_name + ':' + password + '@' + host + '/' + database_name)


def create_table():
    Base.metadata.create_all(engine)


def connection_handler():
    session_factory = sessionmaker(bind=create_engine())
    Session = scoped_session(session_factory)
    sesh = Session()
    return sesh


create_table()
test = process_timer.ProcessRunTimeTracker("pycharm")
test.start()


def add_timer_to_db():
    connection_handler().add(test)
    connection_handler().commit()

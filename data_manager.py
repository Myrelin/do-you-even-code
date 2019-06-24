import psycopg2
import connection
from datetime import datetime


@connection.connection_handler
def setup_database(cursor):
    cursor.execute(
        """
            CREATE TABLE IDEs (
        ID SERIAL PRIMARY KEY,
        ide_name varchar(255),
        date DATE,
        start_time INT,
        finish_time INT,
        language varchar(255),
        session_closed BIT default 0::bit
        );
        """
    )


@connection.connection_handler
def get_all_sessions(cursor):
    try:
        cursor.execute(
            """
            SELECT * from ides;
            """
        )
        return cursor.fetchall()
    except psycopg2.errors.UndefinedTable:
        setup_database()


@connection.connection_handler
def add_coding_session(cursor, ide_name, start_time):
    date = datetime.now()
    try:
        cursor.execute(
            """
            INSERT INTO ides (ide_name, date, start_time) 
            VALUES (%s, %s, %s)
            """, (ide_name, date, start_time)
        )
        return True
    except psycopg2.IntegrityError:
        return False


@connection.connection_handler
def finish_coding_session(cursor, start_time, finish_time):
    try:
        cursor.execute(
            """
            UPDATE answer SET session_closed = 1, finish_time = ${finish_time}s
            WHERE start_time = ${start_time}s;
            """, {start_time: "start_time", finish_time: "finish_time"}
        )
    except psycopg2.DatabaseError:
        return False


get_all_sessions()

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
        process_id INT,
        language varchar(255),
        date DATE,
        start_time INT,
        finish_time INT,
        total_time INT,
        session_closed BIT default 0::bit
        );
        """
    )


@connection.connection_handler
def get_recent_sessions(cursor):
    try:
        cursor.execute(
            """
            SELECT * from ides
            LIMIT 10;
            """
        )
        return cursor.fetchall()
    except psycopg2.errors.UndefinedTable:
        setup_database()

@connection.connection_handler
def get_open_sessions(cursor):
    try:
        cursor.execute(
            """
            SELECT * FROM ides
            WHERE session_closed == 0::bit;
            """
        )
        return cursor.fetchall()
    except psycopg2.errors.UndefinedTable:
        setup_database()


@connection.connection_handler
def add_coding_session(cursor, process_info):
    date = datetime.now()
    try:
        cursor.execute(
            """
            INSERT INTO ides (ide_name, process_id, date, start_time) 
            VALUES (%s, %s, %s, %s)
            """, (process_info['name'], process_info['pid'], date, process_info['create_time'])
        )
        return True
    except psycopg2.IntegrityError:
        return False


@connection.connection_handler
def finish_coding_session(cursor, start_time, finish_time):
    try:
        cursor.execute(
            """
            UPDATE answer SET session_closed = 1::bit, finish_time = ${finish_time}s
            WHERE start_time = ${start_time}s;
            """, {start_time: "start_time", finish_time: "finish_time"}
        )
    except psycopg2.DatabaseError:
        return False


@connection.connection_handler
def get_session_by_pid(cursor, pid):
    try:
        cursor.execute(
            """
            SELECT * FROM ides
            WHERE process_id = {};
            """.format(pid)
        )
        return cursor.fetchone()
    except psycopg2.errors.UndefinedTable:
        setup_database

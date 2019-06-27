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
        total_time varchar(255),
        session_closed BOOLEAN DEFAULT FALSE 
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
            SELECT process_id FROM ides
            WHERE session_closed = FALSE;
            """
        )
        return cursor.fetchall()
    except psycopg2.errors.UndefinedTable:
        setup_database()


@connection.connection_handler
def add_coding_session(cursor, name, proc_id, start_time):
    date = datetime.now()
    try:
        cursor.execute(
            """
            INSERT INTO ides (ide_name, process_id, date, start_time) 
            VALUES (%s, %s, %s, %s)
            """, (name, proc_id, date, start_time)
        )
        return True
    except psycopg2.errors.UndefinedTable:
        setup_database()


@connection.connection_handler
def finish_coding_session(cursor, pid):
    try:
        cursor.execute(
            """
            UPDATE ides SET session_closed = True
            WHERE process_id = {};
            """.format(pid)
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


@connection.connection_handler
def get_open_sessions(cursor):
        cursor.execute(
            """
            SELECT process_id FROM ides
            WHERE session_closed = FALSE
            """
        )
        return cursor.fetchall()

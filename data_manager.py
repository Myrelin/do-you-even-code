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
        last_modified INT,
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
            SELECT * from ides;
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
            INSERT INTO ides (ide_name, process_id, date, start_time, last_modified) 
            VALUES (%s, %s, %s, %s, %s)
            """, (name, proc_id, date, start_time, start_time)
        )
        return True
    except psycopg2.errors.UndefinedTable:
        setup_database()


@connection.connection_handler
def update_last_modified_time(cursor, pid, last_modified):
    try:
        cursor.execute(
            """
            UPDATE ides
            SET last_modified = {}
            WHERE process_id = {} AND session_closed = FALSE
            """.format(last_modified, pid)
        )
    except psycopg2.IntegrityError:
        pass


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

@connection.connection_handler
def close_session(cursor, pid):
    cursor.execute(
        """
        UPDATE ides SET session_closed = TRUE
        WHERE process_id = {}
        """.format(pid)
    )

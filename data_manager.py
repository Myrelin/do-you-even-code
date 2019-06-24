import psycopg2

import connection
from datetime import datetime


# @connection.connection_handler
# def add_question(cursor, question):
#     question['submission_time'] = datetime.now()
#     question['vote_number'] = 0
#     question['view_number'] = 0
#     cursor.execute("""INSERT INTO question (submission_time, view_number, vote_number, title, message, user_id)
#         VALUES(%s, %s, %s, %s, %s, %s)""", (
#         question['submission_time'], question['view_number'], question['vote_number'], question['title'],
#         question['message'], question['user_id']))
#     cursor.execute("SELECT * FROM question")
#     result = cursor.fetchall()
#     return result

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
        time_spent INT,
        language varchar(255),
        session_closed BIT default 0
        );
        """
    )

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

# def finish_coding_session(cursor, ):



setup_database()

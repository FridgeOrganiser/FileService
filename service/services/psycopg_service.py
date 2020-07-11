from psycopg2 import connect, sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import errors

from constants import (
    POSTGRESQL_PASSWORD,
    POSTGRESQL_USER,
    POSTGRESQL_DB_NAME
)


def get_service_db_connection_cursor():
    """Function for getting psycopg2.cursor object for db querying."""
    connection = connect(f"""user={POSTGRESQL_USER} password='{POSTGRESQL_PASSWORD}' """)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    return cursor


def create_service_db():
    """Function for creating database for File Service."""
    cursor = get_service_db_connection_cursor()
    try:
        cursor.execute(sql.SQL(f"""CREATE DATABASE "{POSTGRESQL_DB_NAME}";"""))
        print(">>> Database Created.")
    except errors.lookup("42P04"):  # 42P04 - stands for Duplicate Database Error of psycopg2
        print(f">>> Database with name: {POSTGRESQL_DB_NAME}, already exists")


def drop_service_db():
    """Function for dropping service database."""
    cursor = get_service_db_connection_cursor()
    try:
        cursor.execute(sql.SQL(f"""DROP DATABASE "{POSTGRESQL_DB_NAME}";"""))
        print(f"Deleted database: {POSTGRESQL_DB_NAME}")
    except errors.lookup("3D000"):  # 3D000 - stands for Invalid Catalog Name error of psycopg2
        print(f"Database with name: {POSTGRESQL_DB_NAME} is not exists.")

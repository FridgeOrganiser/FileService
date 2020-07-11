from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from constants import (
    POSTGRESQL_USER,
    POSTGRESQL_HOST,
    POSTGRESQL_DB_NAME,
    POSTGRESQL_PASSWORD
)
from service.models.image_model import Image, Base


class PostgresSetup(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(PostgresSetup, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.dsn = f"""postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}/{POSTGRESQL_DB_NAME}"""
        self.postgres_engine = create_engine(self.dsn)
        self.session_config = sessionmaker(bind=self.postgres_engine)

    @contextmanager
    def get_session_scope(self):
        session = self.session_config()
        try:
            yield session
            session.commit()
        except Exception as err:
            # TODO: Change it in nearest future to some specific error!
            print(err)
            session.rollback()
        finally:
            session.close()


pg = PostgresSetup()


class PG_Query:
    @staticmethod
    def create_general_table():
        Base.metadata.create_all(bind=pg.postgres_engine)
        print(">>> Created general table for File Service.")

    @staticmethod
    def create_new_entity(**kwargs):
        if not kwargs:
            raise ValueError(f"Incorrect input data, expect dict with values, got: {kwargs}")

        with pg.get_session_scope() as session:
            image_entity = Image(**kwargs)
            session.add(image_entity)

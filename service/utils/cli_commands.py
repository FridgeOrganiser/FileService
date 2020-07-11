from service.services.psycopg_service import create_service_db, drop_service_db
from service.services.postgres_service import PG_Query
from flask import Flask
import click
from flask.cli import with_appcontext


@click.command("setup-db")
@with_appcontext
def setup_db():
    """Command in order to setup db for service."""
    create_service_db()


@click.command("create-table")
@with_appcontext
def create_table():
    """Command for creating general table."""
    PG_Query.create_general_table()


@click.command("drop-db")
@with_appcontext
def drop_database():
    """Command fro dropping existing service database."""
    drop_service_db()


def init_cli_commands(app: Flask):
    if not isinstance(app, Flask):
        raise TypeError("App should be instance of Flask application")

    app.cli.add_command(setup_db)
    app.cli.add_command(create_table)
    app.cli.add_command(drop_database)

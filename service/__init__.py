"""Module for defining flask app."""
from flask import Flask
from flask_restful import Api
from service.utils.cli_commands import init_cli_commands


app = Flask("__name__")
api = Api(app)
app.config['UPLOAD_FOLDER'] = 'files/'
init_cli_commands(app)

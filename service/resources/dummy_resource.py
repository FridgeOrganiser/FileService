"""Module for defining basic resource for testing purposes"""
from flask import jsonify
from flask_restful import Resource
from flask_api import status
from flask.wrappers import Response
from service import api


class DummyResource(Resource):
    """Basic resource for testing if service is up and running."""
    def get(self):
        """GET method of resource
            Returns:
                Response: response object with related status
        """
        return jsonify({"Message:": "Hello World"},
                       status.HTTP_200_OK)


api.add_resource(DummyResource, '/')

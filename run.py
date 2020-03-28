"""Module for running whole project"""
from service import app
from service.resources.dummy_resource import DummyResource

if __name__ == "__main__":
    app.run("localhost", 5000)

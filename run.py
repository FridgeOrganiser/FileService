"""Module for running whole project"""
from service import app
from service.resources.dummy_resource import DummyResource
from service.resources.load_resource import FileLoadingResource

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

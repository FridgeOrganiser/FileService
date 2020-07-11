"""Module for defining resource for loading files."""
from flask import jsonify, request
from flask_restful import Resource
from flask_api import status
from PIL import Image

from service import api
from service.utils.utils import (
    get_image_hash_value, is_input_file_correct,
    save_file_and_get_location
)
from service.services.postgres_service import PG_Query


class FileLoadingResource(Resource):
    """File Loading resource for managing image loading into system."""

    def post(self):
        """POST method of resource for downloading user images to system.
                Returns:
                    Response: response object with related status
                Raises:
                    TypeError: in case of objects incorrect types
        """
        if "input_img" in request.files:
            input_file = request.files["input_img"]
            file_name = input_file.filename

            if not is_input_file_correct(file_name):
                raise TypeError("Unsupported File Type")
            
            current_image = Image.open(input_file.stream)
            image_hash = get_image_hash_value(current_image)
            image_location = save_file_and_get_location(current_image, file_name)
            image_size = len(current_image.tobytes())

            PG_Query.create_new_entity(image_hash=image_hash,
                                       image_location=image_location,
                                       image_size=image_size,
                                       image_name=file_name)

            return jsonify(
                {"message": "Created new image entity"},
                status.HTTP_200_OK
            )


api.add_resource(FileLoadingResource, '/load')

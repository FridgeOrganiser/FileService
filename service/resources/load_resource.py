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


class FileLoadingResource(Resource):

    def post(self):

        if "input_img" in request.files:
            input_file = request.files["input_img"]
            file_name = input_file.filename

            if not is_input_file_correct(file_name):
                raise TypeError("Unsupported File Type")

            import pdb;pdb.set_trace()
            
            current_image = Image.open(input_file.stream)
            image_hash = get_image_hash_value(current_image)
            image_location = save_file_and_get_location(current_image, file_name)
            image_size = len(current_image.tobytes())

            print(image_hash, image_location, image_size)

            return jsonify({}, status.HTTP_200_OK)


api.add_resource(FileLoadingResource, '/load')
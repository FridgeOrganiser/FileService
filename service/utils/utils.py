from PIL import Image, JpegImagePlugin
from PIL.ImageFile import ImageFile
import hashlib
import re

from service import app
from constants import FILE_NAME_MATCH


def is_input_file_correct(file_name):
    """Function for checking rather the file name is correct or not.
        Args:
            file_name (str): Name of input image file.
        Returns:
            True: if file name is correct, False otherwise
    """
    if not isinstance(file_name, str):
        raise TypeError("File Name should be - str - type")
    
    return True if re.match(FILE_NAME_MATCH, file_name) else False


def get_image_hash_value(image_obj):
    """Function for getting hash value from image.
        Args:
            image_obj (ImageFile): image object.
        Returns:
            str: hash value
        Raises:
            TypeError: if image path isn't an image object.
    """
    if not isinstance(image_obj, ImageFile):
        raise TypeError("Image obj should be a ImageFile type")

    img_bytes = image_obj.tobytes()
    sha_256_value = hashlib.sha256()
    sha_256_value.update(img_bytes)
    
    return sha_256_value.hexdigest()


def save_file_and_get_location(image_instance, file_name):
    """Function for saving image into file system and returning final location.
        Args:
            image_instance (ImageFile): image object.
            file_name (str): String file name.
        Returns:
            str: location of image
    """
    image_location = f"""{app.config["UPLOAD_FOLDER"]}{file_name}"""
    image_instance.save(image_location)

    return image_location

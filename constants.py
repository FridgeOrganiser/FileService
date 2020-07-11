"""Module for storing constants variables."""
import os
import re
from dotenv import load_dotenv
load_dotenv()

# <regexes>  ---------------------------------------------------

FILE_NAME_MATCH = re.compile(r"(?i).*\.(?:jpg|jpeg|png|gif|bmp|webp)$")

# </regexes> ---------------------------------------------------

# Postgresql credentials ---------------------------------------

POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_DB_NAME = os.getenv("POSTGRESQL_DB_NAME")

# Postgresql credentials ---------------------------------------

# Helper utility functions can be added here
import os
from uuid import uuid4
from urllib.parse import urlparse

def create_unique_file_name(prefix, extension=".txt"):
    random_string = str(uuid4())[0:5]
    return random_string + prefix + extension

def get_netloc(root_url=""):
    return urlparse(root_url).netloc
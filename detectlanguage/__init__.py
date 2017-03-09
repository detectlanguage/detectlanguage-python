__version__ = '1.2.1'

from .exceptions import *
from .configuration import Configuration
from .client import Client
from .api import simple_detect, detect, user_status, languages

configuration = Configuration()
client = Client(configuration)

__version__ = '2.0.0'

from .exceptions import *
from .configuration import Configuration
from .client import Client
from .api import detect, detect_code, detect_batch, account_status, languages

# deprecated functions
from .api import simple_detect, user_status

configuration = Configuration()
client = Client(configuration)

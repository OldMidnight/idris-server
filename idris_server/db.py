import os
from tinydb import TinyDB

status_db = TinyDB(os.getenv('DB_PATH') + '/status.json')
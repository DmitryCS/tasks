import os
from dotenv import load_dotenv


class SQLiteConfig:
    name = os.getenv('dbname', 'db.sqlite')
    url = f'sqlite:///{name}'



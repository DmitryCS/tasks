import os
from dotenv import load_dotenv

load_dotenv()


class SQLiteConfig:
    name = os.getenv('dbname', 'db.sqlite')
    url = rf'sqlite:///{name}'


# class PostgresConfig:
#     name = os.getenv('POSTGRES_NAME', 'tasks')
#     user = os.getenv('POSTGRES_USER', 'admin')
#     password = os.getenv('POSTGRES_PASSWORD', 'qwerty')
#     host = os.getenv('POSTGRES_HOST', 'tasks-db')
#     port = os.getenv('POSTGRES_PORT', '5432')
#     url = rf'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'

class PostgresConfig:
    name = os.getenv('POSTGRES_NAME', 'tasks')
    user = os.getenv('POSTGRES_USER', 'user1')
    password = os.getenv('POSTGRES_PASSWORD', 'qwerty')
    host = os.getenv('POSTGRES_HOST', 'tasks-db')    #0.0.0.0
    port = os.getenv('POSTGRES_PORT', '5432')
    url = rf'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'

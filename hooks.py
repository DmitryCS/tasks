from sqlalchemy import create_engine

from context import Context
from db.database import DataBase


def init_db_sqlite(context: Context):
    uri = r'sqlite:///db.sqlite'
    engine = create_engine(
        name_or_url=uri,
        pool_pre_ping=True,     # if session dropped, it'll automatically launched
    )
    database = DataBase(connection=engine)
    database.check_connection()

    context.set('database', database)

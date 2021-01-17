from sqlalchemy import Column, VARCHAR, VARBINARY

from db.models import BaseModel


class DBUser(BaseModel):

    __tablename__ = 'users'

    login = Column(
        VARCHAR(50),
        unique=True,
        nullable=False,
    )

    password = Column(
        VARBINARY(),
        nullable=False,
    )

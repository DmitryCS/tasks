from api.request.create_user import RequestCreateUserDto
from db.database import DBSession
from db.exceptions import UserExistsException
from db.models.user import DBUser


def create_user(session: DBSession, user: RequestCreateUserDto) -> DBUser:
    new_user = DBUser(
        login=user.login,
        password=user.password,
    )

    if session.get_user_by_login(new_user.login) is not None:
        raise UserExistsException

    session.add_model(new_user)

    return new_user

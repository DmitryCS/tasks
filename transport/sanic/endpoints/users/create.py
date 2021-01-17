from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.create_user import RequestCreateUserDto
from api.response.user import ResponseUserDto
from db.database import DBSession
from transport.sanic.endpoints import BaseEndpoint

from db.queries import user as user_queries
from db.exceptions import DBDataException, DBIntegrityException, UserExistsException


class CreateUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateUserDto(body)

        try:
            db_user = user_queries.create_user(session, request_model)
            session.commit_session()
        except UserExistsException:
            return await self.make_response_json(status=409, message='User already exists')
        except (DBIntegrityException, DBDataException) as e:
            return await self.make_response_json(status=500, message=str(e))

        response_model = ResponseUserDto(db_user)

        return await self.make_response_json(status=201, body=response_model.dump())

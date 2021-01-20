from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicEmployeeNotFound, SanicPasswordHashException

from api.request import RequestAuthEmployeeDto

from db.queries import employee as employee_queries
from db.exceptions import DBEmployeeNotExistsException

from helpers.password import check_hash, CheckPasswordHashException

from helpers.auth import create_token


class AuthEmployeeEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestAuthEmployeeDto(body)

        try:
            db_employee = employee_queries.get_employee(session, login=request_model.login)
        except DBEmployeeNotExistsException as e:
            raise SanicEmployeeNotFound('Employee not found')

        try:
            check_hash(request_model.password, db_employee.password)
        except CheckPasswordHashException:
            raise SanicPasswordHashException('Wrong password')

        payload = {
            'eid': db_employee.id,
        }

        response_body = {
            'Authorization': create_token(payload)
        }

        return await self.make_response_json(
            body=response_body,
            status=200,
        )
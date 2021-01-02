from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateEmployeeDto
from api.response import ResponseEmployeeDto
from transport.sanic.endpoints import BaseEndpoint

from db.queries import employee as employee_queries


class CreateEmployeeEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateEmployeeDto(body)

        db_employee = employee_queries.create_employee(session, request_model)
        session.commit_session()

        response_model = ResponseEmployeeDto(db_employee)

        return await self.make_response_json(body=response_model.dump(), status=201)

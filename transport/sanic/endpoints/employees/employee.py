from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestPatchEmployeeDto
from api.response import ResponseEmployeeDto
from db.database import DBSession
from db.exceptions import DBEmployeeNotExistsException, DBIntegrityException, DBDataException
from db.queries import employee as employee_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicEmployeeNotFound, SanicDBException


class EmployeeEndpoint(BaseEndpoint):

    async def method_patch(
            self, request: Request, body: dict, session: DBSession, eid: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        request_model = RequestPatchEmployeeDto(body)

        try:
            employee = employee_queries.patch_employee(session, request_model, eid)
        except DBEmployeeNotExistsException:
            raise SanicEmployeeNotFound('Employee not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseEmployeeDto(employee)

        return await self.make_response_json(status=200, body=response_model.dump())

    async def method_delete(
            self, request: Request, body: dict, session: DBSession, eid: int, *args, **kwargs
    ) -> BaseHTTPResponse:
        # eid = kwargs['eid']
        try:
            employee = employee_queries.delete_employee(session, eid)
        except DBEmployeeNotExistsException as e:
            raise SanicDBException(str(e))

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)

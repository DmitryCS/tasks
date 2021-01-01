from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateEmployeeDtoSchema(Schema):
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)


class RequestCreateEmployeeDto(RequestDto,RequestCreateEmployeeDtoSchema):
    __schema__ = RequestCreateEmployeeDtoSchema

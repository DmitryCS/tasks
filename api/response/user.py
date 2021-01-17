from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseUserDtoSchema(Schema):
    login = fields.Str(required=True)
    id = fields.Int(required=True)


class ResponseUserDto(ResponseDto, ResponseUserDtoSchema):
    __schema__ = ResponseUserDtoSchema

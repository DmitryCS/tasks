from marshmallow import Schema, fields, post_load

from api.base import RequestDto

from helpers.password import generate_hash


class RequestCreateUserDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)

    @post_load
    def hash_password(self, data: dict, **kwargs) -> dict:
        password = data['password']
        hashed_password = generate_hash(password)
        data['password'] = hashed_password

        return data


class RequestCreateUserDto(RequestDto, RequestCreateUserDtoSchema):
    __schema__ = RequestCreateUserDtoSchema

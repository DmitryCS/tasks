from marshmallow import Schema, ValidationError, EXCLUDE
from sanic.exceptions import SanicException

from api.exceptions import ApiValidationException, ApiResponseValidationException


class RequestDto:
    __schema__: Schema

    def __init__(self, data: dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            raise ApiValidationException(error.messages)
        else:
            self._import(valid_data)

    def _import(self, data: dict):
        for name, field in data.items():
            self.set(name, field)

    def set(self, key, value):
        setattr(self, key, value)


class ResponseDto:
    __schema__: Schema

    def __init__(self, obj: object, many: bool = False):
        # properties = {}
        # for prop in dir(obj):
        #     if not prop.startswith('_') and not prop.endswith('_'):
        #         attr = getattr(obj, prop)
        #         if not callable(attr):
        #             valid_data['prop'] = attr
        if many:
            properties = [self.parse_obj(o) for o in obj]
        else:
            properties = self.parse_obj(obj)

        try:
            self._data = self.__schema__(unknown=EXCLUDE, many=many).load(properties) #, many=many
        except ValidationError as error:
            raise ApiResponseValidationException(error.messages)

    @staticmethod
    def parse_obj(obj: object) -> dict:
        return {
            prop: value
            for prop in dir(obj)
            if not prop.startswith('_')
               and not prop.endswith('_')
               and not callable(value := getattr(obj, prop))
        }

    def dump(self) -> dict:
        return self._data

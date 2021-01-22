from typing import List


class MiddleWareException(Exception):
    pass


class Middleware:
    def process_handler(self, request):
        raise NotImplementedError

    def process_exception(self, exception):
        raise NotImplementedError


class AuthRequiredMiddleware(Middleware):

    def process_handler(self, request):
        print('check auth')

    def process_exception(self, exception):
        pass


class CheckRequestIsInt(Middleware):
    def process_handler(self, request):
        if not isinstance(request, int):
            raise MiddleWareException('request should be int')

    def process_exception(self, exception):
        print(str(exception))


class Endpoint:

    def __init__(self, uri: str, middlewares: List[Middleware]):
        self.uri = uri
        self.middlewares = middlewares

    def handler(self, request):
        for middleware in self.middlewares:
            try:
                middleware.process_handler(request)
            except MiddleWareException as e:
                middleware.process_exception(e)

        print('обработка запроса')


if __name__ == '__main__':

    endpoint = Endpoint(uri='/', middlewares=[AuthRequiredMiddleware(), CheckRequestIsInt()],)

    endpoint.handler(1)
    endpoint.handler('hello')

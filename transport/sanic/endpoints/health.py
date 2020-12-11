from sanic.request import Request
from sanic.response import HTTPResponse, json


async def health_endpoint(request: Request) -> HTTPResponse:
    response = {
        'hello': 'world'
    }

    if 'POST' in request.method:
        response.update(request.json)

    return json(body=response, status=200)
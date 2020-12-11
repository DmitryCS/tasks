from sanic import Sanic

from configs.config import ApplicationConfig
from transport.sanic.routes import get_routes


def configure_app(config: ApplicationConfig):

    app = Sanic(__name__)

    for handler, uri, methods in get_routes(config):
        app.add_route(
            handler=handler,
            uri=uri,
            methods=methods,
        )

    return app

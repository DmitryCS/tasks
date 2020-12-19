from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic.base import SanicEndpoint
from transport.sanic.endpoints.health import HealthEndpoint


def get_routes(config: ApplicationConfig, context: Context) -> Tuple['SanicEndpoint']:
    return (
        HealthEndpoint(config=config, context=context, uri='/', methods=('GET', 'POST')),
    )

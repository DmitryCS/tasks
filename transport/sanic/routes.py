from typing import Tuple

from configs.config import ApplicationConfig
from transport.sanic.base import SanicEndpoint
from transport.sanic.endpoints.health import HealthEndpoint


def get_routes(config: ApplicationConfig) -> Tuple['SanicEndpoint']:
    return (
        HealthEndpoint(config, '/', methods=('GET', 'POST')),
    )

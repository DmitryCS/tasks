from configs.config import ApplicationConfig
from transport.sanic.configure_sanic import configure_app


def main():
    config = ApplicationConfig()
    app = configure_app(config)
    app.run(
        host=config.sanic.host,
        port=config.sanic.port,
        workers=config.sanic.workers,
        debug=config.sanic.debug
    )


if __name__ == '__main__':
    main()

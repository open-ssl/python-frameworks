from aiohttp import web, web_app
from config import START_PORT
from app.routes import set_routes


app = web.Application()


def setup_routes(application: web_app.Application):
    set_routes(application)


if __name__ == "__main__":
    setup_routes(app)
    print("Started an Aiohttp application on 127.0.0.1:{}".format(START_PORT))
    web.run_app(app, port=START_PORT)

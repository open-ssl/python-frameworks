from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from views.views import RootTornadoApp
from config import START_PORT

define('port', default=START_PORT, help='start port')


def main():
    """Construct and serve the tornado application."""
    app = Application([
        ("/", RootTornadoApp)
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://127.0.0.1:%i' % options.port)
    IOLoop.current().start()


if __name__ == "__main__":
    main()

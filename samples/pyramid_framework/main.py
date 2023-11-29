from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from config import START_PORT


def root(request):
    return Response('This is a Pyramid application!')


def main():
    with Configurator() as config:
        config.add_route('root', '/')
        config.add_view(root, route_name='root')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', START_PORT, app)
    print('Listening on http://127.0.0.1:%i' % START_PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()

import cherrypy
from config import START_PORT


class Root(object):
    @cherrypy.expose
    def index(self):
        return 'It is a CherryPy framework!'


def app():
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = START_PORT
    cherrypy.quickstart(Root())


if __name__ == '__main__':
    app()

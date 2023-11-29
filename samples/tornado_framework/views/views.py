from tornado.web import RequestHandler


class RootTornadoApp(RequestHandler):
    """Print 'Hello, it is a Tornado Application!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello, it is a Tornado Application!."""
        self.write("Hello, it is a Tornado Application!")

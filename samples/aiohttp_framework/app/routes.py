from aiohttp import web, web_app

routes = web.RouteTableDef()


@routes.get('/')
async def root_handler(request):
    return web.Response(text="It is an AioHTTP application!")


def set_routes(app: web_app.Application):
    """
    Установка рутов
    :param app: экземпляр приложения
    :return:
    """
    app.add_routes(routes)

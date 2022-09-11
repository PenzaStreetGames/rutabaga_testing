from typing import Optional

from aiohttp.web import Application as AiohttpApplication, \
    run_app as aiohttp_run_app, View as AiohttpView, Request as AoihttpRequest
from aiohttp_apispec import setup_aiohttp_apispec


class Application(AiohttpApplication):
    database: dict = {}


class Request(AoihttpRequest):
    @property
    def app(self) -> Application:
        return super().app


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    from rutabaga.app.web.routes import setup_routes

    setup_routes(app)
    setup_aiohttp_apispec(app, title="Rutabaga", url="/docs/json",
                          swagger_path="/docs")
    aiohttp_run_app(app)

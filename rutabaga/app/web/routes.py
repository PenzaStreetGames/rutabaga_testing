import typing

if typing.TYPE_CHECKING:
    from aiohttp.web_app import Application
from rutabaga.app.kv.routes import setup_routes as setup_kv_routes


def setup_routes(app: "Application"):
    setup_kv_routes(app)

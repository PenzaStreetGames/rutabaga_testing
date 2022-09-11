import typing

if typing.TYPE_CHECKING:
    from aiohttp.web_app import Application


def setup_routes(app: "Application"):
    from rutabaga.app.kv.views import (
        SetKeyValueView,
        GetValueByKeyView,
        ListKeysView,
        ListItemsView,
        ContainsKeyView,
        DeleteKeyView,
        ClearView
    )
    app.router.add_view("/set", SetKeyValueView)
    app.router.add_view("/get", GetValueByKeyView)
    app.router.add_view("/keys", ListKeysView)
    app.router.add_view("/items", ListItemsView)
    app.router.add_view("/contains", ContainsKeyView)
    app.router.add_view("/delete", DeleteKeyView)
    app.router.add_view("/clear", ClearView)

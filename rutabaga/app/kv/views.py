from aiohttp.web_response import json_response

from aiohttp_apispec import docs, request_schema, response_schema, json_schema

from rutabaga.app.kv.schemas import SetKVRequestSchema, SetKVResponseSchema, GetKVRequestSchema, GetKVResponseSchema, \
    ListKeysRequestSchema, ListKeysResponseSchema, ListItemsRequestSchema, ListItemsResponseSchema, \
    ContainsRequestSchema, ContainsResponseSchema, DeleteRequestSchema, DeleteResponseSchema, ClearResponseSchema
from rutabaga.app.web.app import View


class SetKeyValueView(View):
    @docs(tags=["kv"], summary="Задать значение по ключу",
          description="Задаёт значение по ключу")
    @json_schema(SetKVRequestSchema)
    @response_schema(SetKVResponseSchema)
    async def post(self):
        data = await self.request.json()
        key, value = data["key"], data["value"]
        self.request.app.database[key] = value
        return json_response(status=200, data={"key": key, "value": value})


class GetValueByKeyView(View):
    @docs(tags=["kv"], summary="Получить значение по ключу",
          description="Возвращает значение по ключу")
    @request_schema(GetKVRequestSchema)
    @response_schema(GetKVResponseSchema, 200)
    async def post(self):
        data = await self.request.json()
        key = data["key"]
        value = self.request.app.database.get(key, None)
        contains = key in self.request.app.database.keys()
        return json_response(
            status=200,
            # data={"key": key, "contains": contains, "value": value})
            data={"key": value, "contains": contains, "value": key})  # ошибочка, перепутаны key value


class ListKeysView(View):
    @docs(tags=["kv"], summary="Получить список ключей",
          description="Возвращает список ключей хранилища")
    @response_schema(ListKeysResponseSchema, 200)
    async def get(self):
        res = list(self.request.app.database.keys())
        if len(res) > 3:
            res = res[:-1]  # ошибочка, без [:-1]
        return json_response(
            status=200,
            data={
                "keys": res
            })


class ListItemsView(View):
    @docs(tags=["kv"], summary="Получить список пар",
          description="Возвращает список пар ключ-значение")
    @response_schema(ListItemsResponseSchema, 200)
    async def get(self):
        items = [{"key": elem[0], "value": elem[1]} for elem in self.request.app.database.items()][:5]
        # ошибочка, без [1:]
        return json_response(
            status=200,
            data={
                "items": items
            })


class ContainsKeyView(View):
    @docs(tags=["kv"], summary="Проверить наличие ключа в словаре",
          description="Возвращает истина/ложь - есть ли ключ в словаре")
    @request_schema(ContainsRequestSchema)
    @response_schema(ContainsResponseSchema, 200)
    async def post(self):
        data = await self.request.json()
        key = data["key"]
        contains = key in self.request.app.database.keys()
        return json_response(
            status=200,
            data={"key": key, "contains": contains})


class DeleteKeyView(View):
    @docs(tags=["kv"], summary="Удалить ключ из словаря",
          description="Удаляет элемент словаря по ключу")
    @request_schema(DeleteRequestSchema)
    @response_schema(DeleteResponseSchema, 200)
    async def post(self):
        data = await self.request.json()
        key = data["key"]
        value = self.request.app.database.get(key, None)
        contains = key in self.request.app.database.keys()
        if contains:
            self.request.app.database.pop(key)
        # return json_response(
        #     status=200,
        #     data={"key": key, "contains": contains, "value": value})
        return json_response(
            status=200,
            data={"key": key, "contains": False, "value": None})  # ошибочка


class ClearView(View):
    @docs(tags=["kv"], summary="Очистить словарь",
          description="Удаляет из словаря все элементы")
    @response_schema(ClearResponseSchema, 200)
    async def get(self):
        self.request.app.database.clear()
        # return json_response(status=200, data={"clear": True})
        return json_response(status=200, data={"clear": False})  # ошибочка

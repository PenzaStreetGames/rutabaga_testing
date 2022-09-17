from marshmallow import Schema, fields


class KeySchema(Schema):
    key = fields.String(required=True)


class KeyValueSchema(Schema):
    key = fields.String(required=True)
    value = fields.String(required=True)


class ContainsSchema(Schema):
    contains = fields.Boolean(required=True)


class GetKVRequestSchema(KeySchema):
    pass


class SetKVRequestSchema(KeyValueSchema):
    key = fields.String(required=True)
    value = fields.String(required=True)


class ContainsRequestSchema(KeySchema):
    pass


class ListKeysRequestSchema(Schema):
    pass


class ListItemsRequestSchema(Schema):
    pass


class DeleteRequestSchema(KeySchema):
    pass


class ClearRequestSchema(Schema):
    pass


class GetKVResponseSchema(KeyValueSchema, ContainsSchema):
    pass


class SetKVResponseSchema(KeyValueSchema):
    pass


class ContainsResponseSchema(ContainsSchema, KeySchema):
    pass


class ListKeysResponseSchema(Schema):
    keys = fields.Nested(KeySchema, many=True)


class ListItemsResponseSchema(Schema):
    items = fields.Nested(KeyValueSchema, many=True)


class DeleteResponseSchema(KeyValueSchema, ContainsSchema):
    pass


class ClearResponseSchema(Schema):
    clear = fields.Boolean()

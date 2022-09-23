from ninja import Schema
from pydantic import UUID4


class TokenAuth(Schema):
    id: str
    exp: str
    sub: str


class Token(Schema):
    access_token: str
    token_type: str

class MessageOut(Schema):
    message: str

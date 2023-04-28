from enum import Enum
from pydantic import BaseModel
from typing import Union


class PlebError(Enum):
    UNKNOWN = 1
    BAD_PORT = 2


class LoginError:
    code: PlebError

    def __init__(self, code):
        self.code = code


class UserAccountInfo(BaseModel):
    hostname: Union[str, None] = "default"
    tls_cert: Union[str, None] = "default"
    agreed_price: Union[int, None] = 1000
    agreed_denomination: Union[str, None] = "sats"


class NewAccount(BaseModel):
    port: int
    pubkey: str
    name: str
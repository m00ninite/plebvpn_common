from enum import Enum
from pydantic import BaseModel
from typing import Union


class PlebError(Enum):
    UNKNOWN = 1
    BAD_PORT = 2
    NO_CONNECTION = 3
    ACCOUNT_DOES_NOT_EXIST = 4
    ACCOUNT_ALREADY_EXISTS = 5


class LoginError:
    code: PlebError

    def __init__(self, code):
        self.code = code


class UserAccountInfo(BaseModel):
    name: Union[str, None] = "satoshi"
    port: Union[int, None] = 80
    hostname: Union[str, None] = "default"
    pubkey: Union[str, None] = "default"
    agreed_price: Union[int, None] = 1000
    agreed_denomination: Union[str, None] = "sats"
    ovpn_file: Union[str, None] = "/etc/openvpn/ovpns/dummy"


class NewAccount(BaseModel):
    port: int
    pubkey: str
    name: str

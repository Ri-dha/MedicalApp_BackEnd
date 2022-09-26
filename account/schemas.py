import datetime

from ninja import Schema
from pydantic import EmailStr, UUID4

from Backend.utlis.schemas import Token


class AccountOut(Schema):
    id: UUID4
    email: EmailStr
    first_name: str = None
    last_name: str = None
    phone_number: str = None
    address: str = None
    date_joined: datetime.datetime
    account_type: str
class AccountName(Schema):
    first_name: str
    last_name: str

class AccountSignupIn(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    password1: str
    password2: str
    account_type: str


class AccountSignupOut(Schema):
    profile: AccountOut
    token: Token
    profile_id: UUID4


class AccountConfirmationIn(Schema):
    email: EmailStr
    verification_code: str


class AccountUpdateIn(Schema):
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number: str = None
    address: str = None


class AccountSigninOut(Schema):
    profile: AccountOut
    token: Token


class AccountSigninIn(Schema):
    email: EmailStr
    password: str


class PasswordChangeIn(Schema):
    old_password: str
    new_password1: str
    new_password2: str

from ninja import Schema
from pydantic import EmailStr, Field, UUID4
from ninja.orm import create_schema
from typing import List

from account.schemas import AccountName
from clinic.models import TypesOfDoctorChoices

#DocotrTypeOut = create_schema(TypesOfDoctorChoices, exclude=['created', 'updated'])


class DoctorType(Schema):
    id: UUID4
    title: str


class DoctorIn(Schema):
    address: str = None
    gadress: str = None
    city: str = None
    phone: int = None
    specialty: str = None
    email: EmailStr = None
    images: str = None
    is_active: bool = None
    is_featured: bool = None


class DoctorOut(Schema):
    id: UUID4
    full_name : str = None
    address: str = None
    gadress: str = None
    city: str = None
    phone: int = None
    specialty: DoctorType = None
    email: EmailStr = None
    images: str = None
    is_active: bool = None
    is_featured: bool = None


class DoctorDataOut(Schema):
    total_count: int = None
    per_page: int = None
    from_record: int = None
    to_record: int = None
    previous_page: int = None
    next_page: int = None
    current_page: int = None
    page_count: int = None
    data: List[DoctorOut]



class Speciality(Schema):
    name: str = None


class ClinicIn(Schema):
    name: str=None
    address: str=None
    gadress: str=None
    city: str=None
    phone: int=None
    email: EmailStr=None
    website: str=None
    logo: str=None
    images: str=None
    about: str=None

    doctors: List[UUID4] = None
class ClinicOut(Schema):
    id: UUID4
    name: str=None
    address: str=None
    gadress: str=None
    city: str=None

    phone: int=None
    email: EmailStr=None
    website: str=None
    logo: str=None
    images: str=None
    about: str=None

    doctors: List[DoctorOut] = None

class ClinicDoctors(Schema):
    id: UUID4
    clinic: ClinicIn
    doctor: DoctorIn


class DoctorImage(Schema):
    id: UUID4
    image: str

from ninja import Schema
from pydantic import EmailStr, Field, UUID4
from pydantic.schema import date, time

from clinic.schemas import DoctorIn, DoctorOut


class PatientData(Schema):
    full_name: str = None
    id: UUID4
    image: str = None

class TypesOfGender(Schema):
    id: UUID4
    Gender: str


class TypesOfBlood(Schema):
    id: UUID4
    BloodChoices: str


class AppointmentIn(Schema):
    patient: UUID4
    doctor: UUID4
    date: date
    time: time
    reason: str
    approved: bool = None


class AppointmentOut(Schema):
    id: UUID4=None
    patient: PatientData = None
    doctor: DoctorOut = None
    date: date
    time: time
    reason: str
    approved: bool = None


class MedicalHistoryUpdate(Schema):
    gender: str
    age: int
    height: float
    weight: float = None
    blood_group: str = None
    allergies: str = None
    diseases: str = None
    surgeries: str = None
    medications: str = None
    body_mass_index: str = None
    description: str = None


class MedicalHistoryIn(MedicalHistoryUpdate):
    patient: UUID4


class MedicalHistoryOut(Schema):
    id: UUID4
    gender: TypesOfGender
    age: int
    height: float
    weight: float = None
    blood_group: TypesOfBlood = None
    allergies: str = None
    diseases: str = None
    surgeries: str = None
    medications: str = None
    body_mass_index: str = None
    description: str = None
    patient: PatientData


class PrescriptionIn(Schema):
    appointment: UUID4
    name: str = None
    medicines: str = None
    dosage: str = None
    frequency: str = None
    quantity: str = None
    duration: str = None
    description: str = None


class PrescriptionOut(Schema):
    id: UUID4
    name: str = None
    medicines: str = None
    dosage: str = None
    frequency: str = None
    quantity: str = None
    duration: str = None
    description: str = None


class FavouriteDoctors(Schema):
    id: UUID4
    patient: PatientData
    doctor: DoctorIn


class PatientImageIn(Schema):
    patient: UUID4
    image: str

class PatientImageOut(Schema):
    id: UUID4
    patient: UUID4
    image: str

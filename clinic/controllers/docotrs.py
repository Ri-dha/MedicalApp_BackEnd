from http import HTTPStatus

from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from typing import List
from Backend.utlis.premission import AuthBearer
from Backend.utlis.schemas import MessageOut
from Backend.utlis.utils import response
from clinic.models import Doctor, TypesOfDoctorChoices
from clinic.schemas import DoctorIn, DoctorOut
from patient.models import Appointment
from patient.schemas import AppointmentOut

doctor_controller = Router(tags=['Doctor'])


@doctor_controller.put('/doctor',
                       auth=AuthBearer(), response={200: MessageOut, 403: MessageOut})
def register(request, payload: DoctorIn):
    doctor = Doctor.objects.filter(user=request.auth)
    payload = payload.dict()
    specialty = payload.pop('specialty')
    specialty_ = TypesOfDoctorChoices.objects.get(title=specialty)
    doctor.update(**payload, specialty=specialty_)

    if doctor:
        return 200, {'message': 'Doctor updated successfully'}
    else:
        return 403, {'message': 'An error occurred, please try again.'}


@doctor_controller.get('/doctor/get', auth=AuthBearer(), response={200: DoctorOut, 403: MessageOut})
def get_doctor(request):
    try:
        user = get_object_or_404(Doctor, user=request.auth)
    except:
        return response(HTTPStatus.BAD_REQUEST, {'message': 'token missing'})
    return response(HTTPStatus.OK, user)


@doctor_controller.get('/doctors/all', response=List[DoctorOut])
def get_all_doctors(request):
    doctors = Doctor.objects.all()
    return doctors


@doctor_controller.get('/doctors/{specialty}', response=List[DoctorOut])
def get_doctors_by_specialty(request, specialty: str):
    doctors = Doctor.objects.filter(specialty__title=specialty)
    return doctors


@doctor_controller.get('/doctors/{specialty}/{city}', response=List[DoctorOut])
def get_doctors_by_specialty_and_city(request, specialty: str, city: str):
    doctors = Doctor.objects.filter(specialty__title=specialty, city=city)
    return doctors


@doctor_controller.get('appointment/show', auth=AuthBearer(), response={200: AppointmentOut, 403: MessageOut})
def get_appointment(request):
    appointment = Appointment.objects.get(doctor__user=request.auth)
    return 200, appointment


@doctor_controller.get('/search', auth=None, response={
    200: List[DoctorOut],
    404: MessageOut
})
def search_doctors(request, search: str):
    doctors = Doctor.objects.filter(

        Q(specialty__title__icontains=search) |
        Q(city__icontains=search)

    )
    if doctors:
        return 200, doctors
    return 404, {'message': 'No products found'}

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
from patient.schemas import AppointmentOut, AppointmentIn

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



@doctor_controller.get('/search', auth=None, response={
    200: List[DoctorOut],
    404: MessageOut
})
def search_doctors(request, search: str=None):

    doctors = Doctor.objects.filter(
        Q(specialty__title__icontains=search) |
        Q(city__icontains=search)

    )
    if doctors:
        return 200, doctors
    return 404, {'message': 'No doctors found'}

@doctor_controller.get('appointment/show/all', auth=AuthBearer(), response=List[AppointmentOut])
def get_all_appointment(request):
    appointments = Appointment.objects.filter(doctor__user=request.auth)
    return appointments

@doctor_controller.get('appointment/show/{pk}', auth=AuthBearer(), response={200: AppointmentOut, 403: MessageOut})
def get_appointment(request, pk: str):
    appointment = Appointment.objects.get(id=pk)
    return 200, appointment


@doctor_controller.put('appointment/{pk}', auth=AuthBearer(), response={200: MessageOut, 403: MessageOut})
def update_appointment(request, pk: str, approved: bool):
    appointment = Appointment.objects.filter(id=pk)
    appointment.update(approved=approved)
    return 200, {'message': 'Appointment updated successfully'}

@doctor_controller.get('/doctors/isfeatured', response=List[DoctorOut])
def get_featured_doctors(request):
    doctors = Doctor.objects.filter(is_featured=True)
    print(Doctor.objects.all())
    return doctors



@doctor_controller.get('/doctors/{specialty}/{city}', response=List[DoctorOut])
def get_doctors_by_specialty_and_city(request, specialty: str, city: str):
    doctors = Doctor.objects.filter(specialty__title=specialty, city=city)
    return doctors

@doctor_controller.get('/doctors/{specialty}', response=List[DoctorOut])
def get_doctors_by_specialty(request, specialty: str):
    doctors = Doctor.objects.filter(specialty__title=specialty)
    return doctors






from http import HTTPStatus

from django.shortcuts import get_object_or_404
from ninja import Router
from typing import List
from Backend.utlis.premission import AuthBearer
from Backend.utlis.schemas import MessageOut
from Backend.utlis.utils import response
from clinic.models import Doctor, TypesOfDoctorChoices
from clinic.schemas import DoctorIn, DoctorOut

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


@doctor_controller.get('/doctor/get',auth=AuthBearer(), response={200: DoctorOut, 403: MessageOut})
def get_doctor(request):
    try:
        user = get_object_or_404(Doctor, user=request.auth)
    except:
        return response(HTTPStatus.BAD_REQUEST, {'message': 'token missing'})
    return response(HTTPStatus.OK, user)

@doctor_controller.get('/doctors/all',response=List[DoctorOut])
def get_all_doctors(request):
    doctors = Doctor.objects.all()
    return doctors

@doctor_controller.get('/doctors/{specialty}',response=List[DoctorOut])
def get_doctors_by_specialty(request,specialty:str):
    doctors = Doctor.objects.filter(specialty__title=specialty)
    return doctors


@doctor_controller.get('/doctors/{specialty}/{city}',response=List[DoctorOut])
def get_doctors_by_specialty_and_city(request,specialty:str,city:str):
    doctors = Doctor.objects.filter(specialty__title=specialty,city=city)
    return doctors


# @doctor_controller.get('/doctors/{city}',response=List[DoctorOut])
# def get_doctors_by_city(request,city:str):
#     doctors = Doctor.objects.get(city=city)
#     return doctors
# @doctor_controller.get('/doctors/{first_name}',response=List[DoctorOut])
# def get_doctors_by_first_name(request,first_name:str):
#     doctors = Doctor.objects.get(first_name=first_name)
#     return doctors

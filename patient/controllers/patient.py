from http import HTTPStatus
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router,File,NinjaAPI
from ninja.files import UploadedFile
from pydantic import UUID4

from Backend.utlis.premission import AuthBearer
from Backend.utlis.schemas import MessageOut
from Backend.utlis.utils import response
from clinic.models import Doctor
from patient.models import MedicalHistory, Patient, TypeOfGenderChoices, TypeOfBloodChoices, Appointment, Prescription,FavouriteDoctors
from patient.schemas import PatientData, MedicalHistoryIn, MedicalHistoryOut, \
    AppointmentIn, MedicalHistoryUpdate, PrescriptionOut, AppointmentOut, PatientImageOut, PatientImageIn, \
    PrescriptionIn, FavouriteDoctorsOut, FavouriteDoctorsIn

patient_controller = Router(tags=['Patient'])



@patient_controller.post('patient/image', auth=AuthBearer(), response={200: MessageOut, 403: MessageOut})
def post_patient_image(request, file: UploadedFile = File(...)):
    patient = Patient.objects.filter(user=request.auth)
    patient.update(image=file)
    return 200, {'message': 'Image uploaded successfully'}



@patient_controller.get('/patient/me', auth=AuthBearer(), response={200: PatientData, 400: MessageOut})
def me(request):
    try:
        patient = Patient.objects.get(user=request.auth)
        return 200, patient
    except:
        return response(HTTPStatus.BAD_REQUEST, {'message': 'Bad request'})


@patient_controller.get('/patient/medical_history', auth=AuthBearer(),
                        response={200: MedicalHistoryOut, 403: MessageOut})
def get_medical_history(request):
    try:
        patient = get_object_or_404(Patient, user=request.auth)
    except:
        return response(HTTPStatus.BAD_REQUEST, {'message': 'token missing'})
    medical_history = MedicalHistory.objects.get(patient=patient)
    return response(HTTPStatus.OK, medical_history)


@patient_controller.post('/patient/medical_history', auth=AuthBearer(), response={200: MessageOut, 403: MessageOut})
def upload_medical_history(request, payload: MedicalHistoryIn):
    patient_instance = Patient.objects.get(id=payload.patient)

    try:
        MedicalHistory.objects.get(patient=patient_instance)
        return 403, {'message': 'Medical history already exists'}
    except MedicalHistory.DoesNotExist:
        payload = payload.dict()
        payload.pop('patient')
        gender = payload.pop('gender')
        blood_group = payload.pop('blood_group')
        gender_ = TypeOfGenderChoices.objects.get(Gender=gender)
        blood_group_ = TypeOfBloodChoices.objects.get(BloodChoices=blood_group)
        MedicalHistory.objects.create(**payload, patient=patient_instance, gender=gender_, blood_group=blood_group_)
        return 200, {'message': 'Medical history created successfully'}


@patient_controller.put('/patient/medical_history/{pk}', auth=AuthBearer(), response={200: MessageOut, 403: MessageOut})
def update_medical_history(request, pk: UUID4, payload: MedicalHistoryUpdate):
    medical_history = MedicalHistory.objects.filter(id=pk)
    payload = payload.dict()
    gender = payload.pop('gender')
    blood_group = payload.pop('blood_group')
    gender_ = TypeOfGenderChoices.objects.get(Gender=gender)
    blood_group_ = TypeOfBloodChoices.objects.get(BloodChoices=blood_group)
    medical_history.update(**payload, gender=gender_, blood_group=blood_group_)
    return 200, {'message': 'Medical history updated successfully'}
@patient_controller.get('/patient/favdocs', auth=AuthBearer(), response={200: List[FavouriteDoctorsOut], 403: MessageOut})
def get_favdocs(request):
    patient = Patient.objects.get(user=request.auth)
    favdocs = FavouriteDoctors.objects.filter(patient=patient)
    return 200, favdocs


@patient_controller.post('/patient/favdocs', auth=AuthBearer(), response={200: MessageOut, 403: MessageOut})
def add_favdocs(request, payload: FavouriteDoctorsIn):
    patient = Patient.objects.get(user=request.auth)
    doctor = Doctor.objects.get(id=payload.doctor)
    favdoc = FavouriteDoctors.objects.create(patient=patient, doctor=doctor)
    favdoc.save()
    return 200, {'message': 'Favdoc added successfully'}

@patient_controller.delete('/patient/favdocs/{pk}', auth=AuthBearer(), response={200: MessageOut, 403: MessageOut})
def delete_favdocs(request, pk: UUID4):
    favdoc = FavouriteDoctors.objects.get(id=pk)
    favdoc.delete()
    return 200, {'message': 'Favdoc deleted successfully'}









# @patient_controller.post('patient/image', auth=AuthBearer(), response={200: PatientImageOut, 403: MessageOut})
# def upload(request,payload:PatientImageIn,image:UploadedFile):
#     image = payload.dict()
#     new_image = PatientImage.objects.create(**image)
#     if image is not None:
#         new_image.image = image
#         new_image.save()
#
#     return 200, PatientImage

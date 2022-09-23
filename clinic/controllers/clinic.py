from ninja import Router

from Backend.utlis.premission import AuthBearer
from Backend.utlis.schemas import MessageOut
from Backend.utlis.utils import response
from clinic.models import Clinic
from clinic.schemas import ClinicIn, ClinicOut

clinic_controller = Router(tags=['Clinic'])


@clinic_controller.post('clinic', auth=AuthBearer(), response={200: ClinicOut, 403: MessageOut})
def clinic_create(request, payload: ClinicIn):
    if request.auth.is_staff:
        try:
            Clinic.objects.get(name=payload.name)
            return 403, {'message': 'Clinic already exists'}
        except Clinic.DoesNotExist:
            payload = payload.dict()
            doctors_ = payload.pop('doctors')

            clinic = Clinic.objects.create(**payload)
            clinic.save()
            clinic.doctors.add(*doctors_)
            return 200, clinic

@clinic_controller.get('clinic/show/{pk}', auth=AuthBearer(), response={200: ClinicOut , 403: MessageOut})
def get_clinic(request, pk: str):
    clinic = Clinic.objects.get(id=pk)
    return 200, clinic

@clinic_controller.put('clinic/update/{pk}', auth=AuthBearer(), response={200: ClinicOut, 403: MessageOut})
def update_clinic(request, pk: str, payload: ClinicIn):
    if request.auth.is_staff:
        try:
            clinic = Clinic.objects.get(id=pk)
            clinic.name = payload.name
            clinic.address = payload.address
            clinic.save()
            return 200, clinic
        except Clinic.DoesNotExist:
            return 403, {'message': 'Clinic does not exist'}
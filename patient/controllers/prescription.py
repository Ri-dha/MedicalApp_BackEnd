from ninja import Router

from Backend.utlis.premission import AuthBearer
from Backend.utlis.schemas import MessageOut
from patient.models import Appointment, Prescription
from patient.schemas import PrescriptionIn, PrescriptionOut

prescription_controller = Router(tags=['Prescription'])


@prescription_controller.post('prescription', auth=AuthBearer(), response={200: PrescriptionOut, 403: MessageOut})
def prescription(request, payload: PrescriptionIn):
    appointment_instance = Appointment.objects.get(id=payload.appointment)
    try:
        Prescription.objects.get(appointment=appointment_instance)
        return 403, {'message': 'Prescription already exists'}
    except Prescription.DoesNotExist:
        payload = payload.dict()
        payload.pop('appointment')
        prescription = Prescription.objects.create(**payload, appointment=appointment_instance)
        prescription.save()
        return 200, prescription


@prescription_controller.get('prescription/show/{pk}', response={200: PrescriptionOut, 403: MessageOut})
def get_prescription(request, pk: str):
    prescription = Prescription.objects.get(id=pk)
    return 200, prescription

from typing import List

from ninja import Router


from Backend.utlis.premission import AuthBearer
from Backend.utlis.schemas import MessageOut
from clinic.models import Doctor
from patient.models import Patient, Appointment
from patient.schemas import AppointmentIn, AppointmentOut

appointment_controller = Router(tags=['Appointment'])



@appointment_controller.post('appointment', auth=AuthBearer(), response={200: AppointmentOut, 403: MessageOut})
def appointment(request, payload: AppointmentIn):
    patient_instance = Patient.objects.get(id=payload.patient)
    doctor_instance = Doctor.objects.get(id=payload.doctor)
    try:
        Appointment.objects.get(patient=patient_instance, doctor=doctor_instance)
        return 403, {'message': 'Appointment already exists'}
    except Appointment.DoesNotExist:
        payload = payload.dict()
        payload.pop('patient')
        payload.pop('doctor')
        appointment = Appointment.objects.create(**payload, patient=patient_instance, doctor=doctor_instance)
        return 200, appointment


@appointment_controller.get('appointment/show/{pk}', auth=AuthBearer(), response={200: AppointmentOut, 403: MessageOut})
def get_appointment(request, pk: str):
    appointment = Appointment.objects.get(id=pk)
    return 200, appointment

@appointment_controller.get('appointment/show/all', auth=AuthBearer(), response=List[AppointmentOut])
def get_all_appointment(request):
    appointments = Appointment.objects.filter(patient=request.auth)
    return appointments


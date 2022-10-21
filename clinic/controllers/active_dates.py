from django.db import router
from ninja import Router
from ..models import ActiveDate,Doctor
import datetime
from .create_doctor_schedual_date_and_time import create_doctor_schedual_date_and_time
from ..schemas import WeekDays
from pydantic import UUID4

router = Router(tags=['active_dates'])

@router.post('create_schedual_active_dates')
def create_active_dates(request,doctor_id:UUID4, res: WeekDays):
    try:
        doc = Doctor.objects.get(
            id=doctor_id
        )
        schedual = create_doctor_schedual_date_and_time(
            howManyDays=30, **res.dict())

        for appit in schedual:
            for day in list(appit.values())[0]:
                date = list(day.keys())[0]
                for onetime in list(day.values())[0]:

                    requestedDate = f"{date}, {onetime}"
                    assignedDate = datetime.datetime.strptime(
                        requestedDate, '%Y-%m-%d, %H:%M:%S')

                    try:
                        docdate = ActiveDate.objects.create(
                            datetime=assignedDate, doctor=doc)

                        docdate.save()
                    except:
                        pass
        return {"final": schedual}
    except Doctor.DoesNotExist:
        return {"details": "only doctors are allowed to change their schedual"}
    
    

@router.get('doctor_active_dates')
def doctor_active_dates(request, doctor_id: UUID4):
    doctor = Doctor.objects.get(id=doctor_id)
    active_dates = list(
        doctor.active_date.all().values_list('datetime', flat=True))

    return {
        "profile_id": doctor.id,
        "full name": doctor.full_name,
        "active dates": active_dates,
    }
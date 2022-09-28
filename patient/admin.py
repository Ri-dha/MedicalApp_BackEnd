from django.contrib import admin
from patient.models import *

admin.site.register(Patient)
admin.site.register(PatientImage)
admin.site.register(MedicalHistory)
admin.site.register(Prescription)
admin.site.register(FavouriteDoctors)
admin.site.register(Appointment)
admin.site.register(TypeOfGenderChoices)
admin.site.register(TypeOfBloodChoices)

# Register your models here.

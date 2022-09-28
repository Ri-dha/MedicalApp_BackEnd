from django.contrib import admin

from clinic.models import Doctor, Clinic, Schedule, TypesOfDoctorChoices

admin.site.register(Doctor)
admin.site.register(Clinic)

admin.site.register(Schedule)
admin.site.register(TypesOfDoctorChoices)

# Register your models here.

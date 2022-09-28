import uuid
from django.db import models
from django.contrib.auth import get_user_model

from Backend.utlis.tools import Entity

User = get_user_model()


# Create your models here.


class TypesOfDoctorChoices(Entity):
    GENERAL = 'General'
    Dentist = 'DENTIST'
    Allergist = 'ALLERGIST'
    Anesthesiologist = 'ANESTHESIOLOGIST'
    Cardiologist = 'CARDIOLOGIST'
    Dermatologist = 'DERMATOLOGIST'
    Endocrinologist = 'ENDOCRINOLOGIST'
    Gastroenterologist = 'GASTROENTEROLOGIST'
    Hematologist = 'HEMATOLOGIST'
    Infectious_Disease_Specialist = 'INFECTIOUS DISEASE SPECIALIST'
    Nephrologist = 'NEPHROLOGIST'
    Neurologist = 'NEUROLOGIST'
    Oncologist = 'ONCOLOGIST'
    Ophthalmologist = 'OPHTHALMOLOGIST'
    Orthopedic_Surgeon = 'ORTHOPEDIC SURGEON'
    Otolaryngologist = 'OTOLARYNGOLOGIST'
    Pathologist = 'PATHOLOGIST'
    Pediatrician = 'PEDIATRICIAN'
    Psychiatrist = 'PSYCHIATRIST'
    Pulmonologist = 'PULMONOLOGIST'
    Radiologist = 'RADIOLOGIST'
    Rheumatologist = 'RHEUMATOLOGIST'
    Urologist = 'UROLOGIST'
    Vascular_Surgeon = 'VASCULAR SURGEON'
    Other = 'OTHER'
    title = models.CharField('title', max_length=255, choices=[
        (GENERAL, GENERAL),
        (Dentist, Dentist),
        (Allergist, Allergist),
        (Anesthesiologist, Anesthesiologist),
        (Cardiologist, Cardiologist),
        (Dermatologist, Dermatologist),
        (Endocrinologist, Endocrinologist),
        (Gastroenterologist, Gastroenterologist),
        (Hematologist, Hematologist),
        (Infectious_Disease_Specialist, Infectious_Disease_Specialist),
        (Nephrologist, Nephrologist),
        (Neurologist, Neurologist),
        (Oncologist, Oncologist),
        (Ophthalmologist, Ophthalmologist),
        (Orthopedic_Surgeon, Orthopedic_Surgeon),
        (Otolaryngologist, Otolaryngologist),
        (Pathologist, Pathologist),
        (Pediatrician, Pediatrician),
        (Psychiatrist, Psychiatrist),
        (Pulmonologist, Pulmonologist),
        (Radiologist, Radiologist),
        (Rheumatologist, Rheumatologist),
        (Urologist, Urologist),
        (Vascular_Surgeon, Vascular_Surgeon),
        (Other, Other),
    ])
    is_default = models.BooleanField('is_default')

    def __str__(self):
        return self.title


class Doctor(Entity):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='doctor')
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    gadress = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    specialty = models.ForeignKey(TypesOfDoctorChoices, on_delete=models.SET_NULL, related_name='specialty', null=True,
                                  blank=True)
    image = models.ImageField(upload_to='media/doctors', null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_featured = models.BooleanField(default=False, null=True, blank=True)
    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name





class Clinic(Entity):
    name = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    gadress = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='clinic_logo', blank=True, null=True)
    images = models.ImageField(upload_to='clinic_images', blank=True, null=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    doctors = models.ManyToManyField('Doctor', related_name='clinic')

    def __str__(self):
        return self.name


class Schedule(Entity):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.doctor.user.first_name + ' ' + self.doctor.user.last_name + ' ' + self.day



# class ClinicDoctors(Entity):
#     clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.clinic.name + ' ' + self.doctor.user.first_name + ' ' + self.doctor.user.last_name


# class ratingtype(models.textChoices):
#     OneStar = '1', '1 Star'
#     TwoStar = '2', '2 Star'
#     ThreeStar = '3', '3 Star'
#     FourStar = '4', '4 '
#     FiveStar = '5', '5 '
#
# class rating(Entity):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     rating = models.IntegerField(max_length=1)
#     def __str__(self):
#         return self.patient.user.first_name + ' ' + self.patient.user.last_name + ' ' + self.doctor.user.first_name + ' ' + self.doctor.user.last_name

# class Report(Entity):
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     def __str__(self):
#         return self.appointment.patient.user.first_name + ' ' + self.appointment.patient.user.last_name + ' ' + self.appointment.doctor.user.first_name + ' ' + self.appointment.doctor.user.last_name

# class PrescriptionImage(Entity):
#     prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='prescription_images')
#
#     def __str__(self):
#         return self.prescription.appointment.patient.user.first_name + ' ' + self.prescription.appointment.patient.user.last_name + ' ' + self.prescription.appointment.doctor.user.first_name + ' ' + self.prescription.appointment.doctor.user.last_name

# class LabTest(Entity):
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     result = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name + ' - ' + self.appointment.patient.first_name + ' ' + self.appointment.patient.last_name
#
#
# class LabTestResult(Entity):
#     lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
#     result = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.lab_test.name + ' - ' + self.lab_test.appointment.patient.first_name + ' ' + self.lab_test.appointment.patient.last_name

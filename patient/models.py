from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from clinic.models import Doctor
from clinic.models import Clinic
from Backend.utlis.tools import Entity

# Create your models here.
User = get_user_model()


class Patient(Entity):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='patient')
    image = models.ImageField(upload_to='media/patients', null=True, blank=True)
    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class PatientImage(Entity):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientimage')
    image = models.ImageField(upload_to='patient_images', blank=True, null=True)

    def __str__(self):
        return self.patient.user.first_name + ' ' + self.patient.user.last_name


class TypeOfGenderChoices(Entity):
    QUEEN = 'QUEEN'
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    Gender = models.CharField('gender', max_length=255, choices=
    [
        (QUEEN, QUEEN),
        (MALE, MALE),
        (FEMALE, FEMALE)
    ])
    is_default = models.BooleanField('is_default')

    def __str__(self):
        return self.Gender


class TypeOfBloodChoices(Entity):
    A_plus = 'A+'
    A_neg = 'A-'
    B_plus = 'B+'
    B_neg = 'B-'
    AB_plus = 'AB+'
    AB_neg = 'AB-'
    O_plus = 'O+'
    O_neg = 'O-'
    BloodChoices = models.CharField('blood_choices', max_length=255, choices=[
        (A_plus, A_plus),
        (A_neg, A_neg),
        (B_plus, B_plus),
        (B_neg, B_neg),
        (AB_plus, AB_plus),
        (AB_neg, AB_neg),
        (O_plus, O_plus),
        (O_neg, O_neg)
    ])
    is_default = models.BooleanField('is_default')

    def __str__(self):
        return self.BloodChoices


class MedicalHistory(Entity):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(
        150)])  # in the controller take the age of user and put it here
    gender = models.ForeignKey(TypeOfGenderChoices, on_delete=models.SET_NULL, related_name='Sex', null=True)
    height = models.DecimalField(decimal_places=2, max_digits=10)
    weight = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    blood_group = models.ForeignKey(TypeOfBloodChoices, on_delete=models.SET_NULL, related_name='BloodGroup', null=True,
                                    blank=True)
    allergies = models.CharField(max_length=50, null=True, blank=True)
    diseases = models.CharField(max_length=50, null=True, blank=True)
    surgeries = models.CharField(max_length=50, null=True, blank=True)
    medications = models.CharField(max_length=50, null=True, blank=True)
    body_mass_index = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.patient.user.first_name + ' ' + self.patient.user.last_name


class Appointment(Entity):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.user.first_name + ' ' + self.patient.user.last_name + ' ' + self.doctor.user.first_name + ' ' + self.doctor.user.last_name


class Prescription(Entity):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    medicines = models.CharField(max_length=200, null=True, blank=True)
    dosage = models.CharField(max_length=200, null=True, blank=True)
    frequency = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.appointment.patient.user.first_name + ' ' + self.appointment.patient.user.last_name + ' ' + self.appointment.doctor.user.first_name + ' ' + self.appointment.doctor.user.last_name


class FavouriteDoctors(Entity):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.user.first_name + ' ' + self.patient.user.last_name + ' ' + self.doctor.user.first_name + ' ' + self.doctor.user.last_name

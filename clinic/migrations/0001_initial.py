# Generated by Django 4.1.1 on 2022-09-23 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('gadress', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_featured', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypesOfDoctorChoices',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(choices=[('General', 'General'), ('ALLERGIST', 'ALLERGIST'), ('ANESTHESIOLOGIST', 'ANESTHESIOLOGIST'), ('CARDIOLOGIST', 'CARDIOLOGIST'), ('DERMATOLOGIST', 'DERMATOLOGIST'), ('ENDOCRINOLOGIST', 'ENDOCRINOLOGIST'), ('GASTROENTEROLOGIST', 'GASTROENTEROLOGIST'), ('HEMATOLOGIST', 'HEMATOLOGIST'), ('INFECTIOUS DISEASE SPECIALIST', 'INFECTIOUS DISEASE SPECIALIST'), ('NEPHROLOGIST', 'NEPHROLOGIST'), ('NEUROLOGIST', 'NEUROLOGIST'), ('ONCOLOGIST', 'ONCOLOGIST'), ('OPHTHALMOLOGIST', 'OPHTHALMOLOGIST'), ('ORTHOPEDIC SURGEON', 'ORTHOPEDIC SURGEON'), ('OTOLARYNGOLOGIST', 'OTOLARYNGOLOGIST'), ('PATHOLOGIST', 'PATHOLOGIST'), ('PEDIATRICIAN', 'PEDIATRICIAN'), ('PSYCHIATRIST', 'PSYCHIATRIST'), ('PULMONOLOGIST', 'PULMONOLOGIST'), ('RADIOLOGIST', 'RADIOLOGIST'), ('RHEUMATOLOGIST', 'RHEUMATOLOGIST'), ('UROLOGIST', 'UROLOGIST'), ('VASCULAR SURGEON', 'VASCULAR SURGEON'), ('OTHER', 'OTHER')], max_length=255, verbose_name='title')),
                ('is_default', models.BooleanField(verbose_name='is_default')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('day', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='doctor_images')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialty', to='clinic.typesofdoctorchoices'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('gadress', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='clinic_logo')),
                ('images', models.ImageField(blank=True, null=True, upload_to='clinic_images')),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                ('doctors', models.ManyToManyField(related_name='clinic', to='clinic.doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

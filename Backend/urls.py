"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from django.conf.urls.static import static

from Backend import settings
from account.controllers import auth_controller
from patient.controllers.patient import patient_controller
from clinic.controllers.docotrs import doctor_controller
from clinic.controllers.clinic import clinic_controller
from clinic.controllers.active_dates import router as active_dates_controller
from patient.controllers.appointment import appointment_controller
from patient.controllers.prescription import prescription_controller

api = NinjaAPI()
api.add_router('account', auth_controller)
api.add_router('patient', patient_controller)
api.add_router('doctor', doctor_controller)
api.add_router('appointment', appointment_controller)
api.add_router('prescription', prescription_controller)
api.add_router('active_dates', active_dates_controller)
api.add_router('clinic', clinic_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
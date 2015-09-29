"""
HealthNet Appointments urls
"""

from django.conf.urls import url

from . import views

app_name = 'appointments'  # namespace

urlpatterns = [
    # The URL to create an appointment
    url(r'^(?P<username>\w+)/create/', views.createAppointment, name='createAppointment'),
]
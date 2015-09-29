"""
HealthNet Appointments Views
"""
from django.shortcuts import render
from .forms import AppointmentForm
from .models import Appointment
from django.http import HttpResponseRedirect, HttpResponse

def createAppointment(request, username):
    form = AppointmentForm()

    if request.method == 'POST':
        appointment = Appointment()

        appointment.title = request.POST['title']
        appointment.when = request.POST['when']
        appointment.patient = username
        appointment.doctor = request.POST['doctor']
        appointment.hospital = request.POST['hospital']
        appointment.room = request.POST['room']
        appointment.reason = request.POST['reason']

        appointment.save()
    else:
        print("boner")
"""
HealthNet Profile Models
"""
from django.db import models
from django.contrib.auth.models import User

# The User model represents the basic information for every Healthnet user.
class HealthNetUser(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('A', 'Admin'),
        ('N', 'Nurse'),
    )
    user = models.OneToOneField(User)
    accountType = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='P')
    # username = models.CharField(max_length=254, unique=True)
    # email = models.CharField(max_length=100, default="")
    isNew = models.BooleanField(default=True)

# The Patient model is a child of User and contains fields specific to a patient.
class Patient(HealthNetUser):
    birthDate = models.DateField()
    height = models.CommaSeparatedIntegerField(max_length=5)
    weight = models.IntegerField()
    insurance = models.CharField(max_length=200)
    allergies = models.TextField()
    conditions = models.TextField()
    prescriptions = models.TextField()
    hospitalPref = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

# The Contact model contains contact information for a person.  Each User has many Contacts.
class Contact(models.Model):
    firstName = models.CharField(max_length=32)
    middleInitial = models.CharField(max_length=1)
    lastName = models.CharField(max_length=64)
    phoneNumber = models.CommaSeparatedIntegerField(max_length=10)
    address = models.CharField(max_length=1000)
    RELATION_CHOICES = (
        ('se', 'Self'),
        ('ga', 'Guardian'),
        ('sp', 'Spouse'),
        ('fa', 'Father'),
        ('mo', 'Mother'),
        ('si', 'Sibling'),
        ('ch', 'Child'),
        ('ot', 'Other'),
    )
    relation = models.CharField(max_length=2, choices=RELATION_CHOICES)
    user = models.ForeignKey(HealthNetUser)

    def __str__(self):
        return self.firstName

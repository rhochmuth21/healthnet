"""
HealthNet Profile Models
"""
from django.db import models

# The User model represents the basic information for every Healthnet user.
class User(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('A', 'Admin'),
        ('N', 'Nurse'),
    )
    accountType = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='P')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    isNew = models.BooleanField(default=True)
    #contactList = []


# THe Contact model contains contact information for a person.  Each User has many Contacts.
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
    user = models.ForeignKey(User)

    def __str__(self):
        return self.firstName


# The Patient model is a child of User and contains fields specific to a patient.
class Patient(User):
    birthDate = models.DateField()
    height = models.CommaSeparatedIntegerField(max_length=5)
    weight = models.IntegerField()
    insurance = models.CharField(max_length=200)
    allergies = models.TextField()
    conditions = models.TextField()
    prescriptions = models.TextField()
    hospitalPref = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    def get_short_name(self):
        pass

    def get_full_name(self):
        pass

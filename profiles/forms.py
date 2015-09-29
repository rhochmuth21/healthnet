"""
HealthNet Profile Forms
"""
from django import forms

from .models import User, Contact, Patient


# This form contains a text field for a username and a password field for a password.
# It is shown on the index page used to login to the system.
class IndexForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'required': 'true', 'placeholder': 'username', 'id': 'username-field'}),
            'password': forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'password', 'id': 'password-field'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstName', 'middleInitial', 'lastName', 'phoneNumber', 'address', 'relation')
        labels = {
            'firstName': 'First Name',
            'middleInitial': 'Middle Initial',
            'lastName': 'Last Name',
            'phoneNumber': 'Phone Number',
            'address': 'Address',
            'relation': 'Relationship',
        }


class EditPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('height', 'weight', 'allergies', 'conditions', 'hospitalPref')
        labels = {
            'height': 'Height',
            'weight': 'Weight',
            'allergies': 'Allergies',
            'conditions': 'Medical Conditions',
            'hospitalPref': 'Preferred Hospital',
        }
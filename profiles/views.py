"""
HealthNet Profile Views
"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import IndexForm, ContactForm, EditPatientForm
from .models import Contact, HealthNetUser, Patient
from django.contrib import messages

# The index view simply renders the index.html template with a blank login form.
def index(request):
    form = IndexForm()

    if request.method == 'POST':
        message = request.POST['error_message']
        return render(request, 'profiles/index.html', {'form': form, 'error_message': message})
    else:
        return render(request, 'profiles/index.html', {'form': form})


def register(request):
    if request.method == 'POST':

        authUser = User()
        authUser.username = request.POST['username']
        authUser.email = request.POST['email']
        authUser.set_password(request.POST['password'])
        authUser.first_name = ""
        authUser.last_name = ""
        authUser.is_active = True
        authUser.is_staff = False
        authUser.is_superuser = False
        authUser.save()

        newUser = Patient()
        newUser.user = authUser
        newUser.isNew = True
        newUser.accountType = 'P'
        newUser.birthDate = "1993-08-21"
        newUser.height = 5, 11
        newUser.weight = 150
        newUser.insurance = ""
        newUser.allergies = ""
        newUser.conditions = ""
        newUser.prescriptions = ""
        newUser.hospitalPref = ""
        newUser.save()

        message = "You're account has been registered!  You can now login."
        messages.add_message(request, messages.INFO, message)

        return HttpResponseRedirect("/")


# The login view takes the form data from the index view and uses it to authenticate
# and log in a user.
def login(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        # the password verified for the user
        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect("/profiles/" + request.POST['username'])
        else:
            message = "This account has been disabled."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect("/")
    else:
        # the authentication system was unable to verify the username and password
        message = "Username and/or password not recognized!"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect("/")

def logout(request):
    auth_logout(request)
    message = "Successfully logged out!"
    messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect("/")

# The viewProfile view obtains the user by userName and displays that user's information.
def viewProfile(request, username):
    if request.user.is_authenticated():
        if request.user.username == username:
            return render(request, 'profiles/patientprofile.html', {'username': username})
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect("/")

# The addContact view presents a form to fill in that adds a new contact to the user.
def addContact(request, username):
    if request.user.is_authenticated():
        if request.user.username == username:
            form = ContactForm()

            if request.method == 'POST':
                contact = Contact()
                contact.address = request.POST['address']
                contact.firstName = request.POST['firstName']
                contact.lastName = request.POST['lastName']
                contact.middleInitial = request.POST['middleInitial']
                contact.phoneNumber = request.POST['phoneNumber']
                contact.relation = request.POST['relation']
                contact.healthnetuser = User.objects.get(username=request.user.username).healthnetuser
                contact.user_id = User.objects.get(username=username).healthnetuser.pk
                contact.save()

                return HttpResponseRedirect("/profiles/" + username)
            else:
                return render(request, 'profiles/addcontact.html', {'form': form, 'username': username})
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect("/")

def editContact(request, username, pk):
    if request.user.is_authenticated():
        if request.user.username == username:
            contact = Contact.objects.get(pk=pk)
            if contact.user_id == User.objects.get(username=request.user.username).healthnetuser.pk:
                if request.method == 'POST':
                    contact.address = request.POST['address']
                    contact.firstName = request.POST['firstName']
                    contact.lastName = request.POST['lastName']
                    contact.middleInitial = request.POST['middleInitial']
                    contact.phoneNumber = request.POST['phoneNumber']
                    contact.relation = request.POST['relation']
                    contact.save()
                    return HttpResponseRedirect("/profiles/" + username)
                else:
                    data = {
                        'address': contact.address,
                        'firstName': contact.firstName,
                        'lastName': contact.lastName,
                        'middleInitial': contact.middleInitial,
                        'phoneNumber': contact.phoneNumber,
                        'relation': contact.relation,
                    }
                    form = ContactForm(data)
                    return render(request, 'profiles/editcontact.html', {'form': form, 'username': username, 'pk': pk})
            else:
                message = "You do not have permission to view the requested page."
                messages.add_message(request, messages.INFO, message)
                return HttpResponseRedirect("/")

        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect("/")

def deleteContact(request, username, pk):
    if request.user.is_authenticated():
        if request.user.username == username:
            contact = Contact.objects.get(pk=pk)
            if contact.user_id == User.objects.get(username=request.user.username).healthnetuser.pk:
                contact.delete()
                return HttpResponseRedirect("/profiles/" + username)
            else:
                message = "You do not have permission to view the requested page."
                messages.add_message(request, messages.INFO, message)
                return HttpResponseRedirect("/")
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect("/")

def editProfile(request, username):
    if request.user.is_authenticated():
        if request.user.username == username:
            aPatient = Patient.objects.get(username=username)
            aForm = EditPatientForm(request.POST, instance=aPatient)
            aForm.save()
            return HttpResponseRedirect("profiles/" + username)
        else:
            message = "You do not have permission to view the requested page."
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect("/")
    else:
        message = "You must login to do that!"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect("/")

# if request.user.is_authenticated():
#     if request.user.username == username:
#         # Do stuff
#     else:
#         message = "You do not have permission to view the requested page."
#         messages.add_message(request, messages.INFO, message)
#         return HttpResponseRedirect("/")
# else:
#     message = "You must login to do that!"
#     messages.add_message(request, messages.INFO, message)
#     return HttpResponseRedirect("/")

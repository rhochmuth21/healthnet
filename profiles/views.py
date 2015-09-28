"""
HealthNet Profile Views
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from .forms import IndexForm, ContactForm
from .models import Contact, User, Patient

# The index view simply renders the index.html template with a blank login form.
def index(request):
    form = IndexForm()

    if request.method == 'POST':
        message = request.POST['error_message']
        return render(request, 'profiles/index.html', {'form': form, 'message': message})
    else:
        return render(request, 'profiles/index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        newUser = Patient()
        newUser.username = request.POST['username']
        newUser.email = request.POST['email']
        newUser.password = request.POST['password']
        newUser.isNew = True
        newUser.accountType = 'P'
        newUser.birthDate = "1993-08-21"
        newUser.height = 5,11
        newUser.weight = 150
        newUser.insurance = ""
        newUser.allergies = ""
        newUser.conditions = ""
        newUser.prescriptions = ""
        newUser.hospitalPref = ""
        newUser.save()

        return HttpResponseRedirect("/profiles/" + request.POST['username'])
    else:
        return render(request, 'profiles/index.html', {'form': form})

# The login view takes the form data from the index view and uses it to authenticate
# and log in a user.
def login(request):
    logout(request)
    if request.POST:
        usr = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usr, password=pwd)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('profiles/' + usr)
    return render_to_response('profiles/index.html')

# The viewProfile view obtains the user by userName and displays that user's information.
def viewProfile(request, userName):
    return render(request, 'profiles/patientprofile.html')

# The addContact view presents a form to fill in that adds a new contact to the user.
def addContact(request, userName):
    form = ContactForm()

    if request.method == 'POST':
        contact = Contact()
        contact.address = request.POST['address']
        contact.firstName = request.POST['firstName']
        contact.lastName = request.POST['lastName']
        contact.middleInitial = request.POST['middleInitial']
        contact.phoneNumber = request.POST['phoneNumber']
        contact.relation = request.POST['relation']
        contact.user = User.objects.get(username=userName)
        contact.save()

        #User.objects.get(username=userName).contactList.append(contact)
        return HttpResponseRedirect("profiles/" + userName)
    else:
        return render(request, 'profiles/addcontact.html', {'form': form, 'userName': userName})

def editContact(request, userName):

    #for person in User.objects.get(username=userName).contactList:
    #look for person with the same name then use them as contact for rest of function

    if request.method == 'POST':
        contact = User.objects.get(username=userName)

        contact.address = request.POST['address']
        contact.firstName = request.POST['firstName']
        contact.lastName = request.POST['lastName']
        contact.middleInitial = request.POST['middleInitial']
        contact.phoneNumber = request.POST['phoneNumber']
        contact.relation = request.POST['relation']
        contact.save()
        return HttpResponseRedirect("profiles/" + userName)
    else:
        #for person in User.objects.get(username=userName).contactList:
        #look for person with the same name then use them as contact for rest of function
        contact = User.objects.get(username=userName)

        data = {
            'address': contact.address,
            'firstName': contact.firstName,
            'lastName': contact.lastName,
            'middleInitial': contact.middleInitial,
            'phoneNumber': contact.phoneNumber,
            'relation': contact.relation,
                }
        form = ContactForm(data)
        return render(request, 'profiles/editcontact.html', {'form': form, 'userName': userName})

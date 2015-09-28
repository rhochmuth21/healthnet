"""
HealthNet Profile URLs
"""
from django.conf.urls import url

from . import views

app_name = 'profiles'  # namespace

urlpatterns = [
    # The root URL links to the index view that displays the login page
    url(r'^$', views.index, name='index'),

    # The register URL links to the register view to create a new user
    url(r'^register/$', views.register, name='register'),

    # The login URL links to the login view which authenticates a user with the given form data
    url(r'^login/$', views.login, name='login'),

    # This URL links to the viewProfile view that displays a user's information
    url(r'^profiles/(?P<userName>\w*)$', views.viewProfile, name='viewProfile'),

    # This URL links to the addContact view which presents a form to add a new user contact
    url(r'^profiles/(?P<userName>\w+)/addcontact$', views.addContact, name='addContact'),

    # This URL links to the editContact view which presents a form to edit their contacts
    url(r'^profiles/(?P<userName>\w+)/editcontact$', views.editContact, name='addContact'),
]

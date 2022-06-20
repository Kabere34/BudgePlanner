from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('register',RegistrationView.as_view(),name="register"),
]

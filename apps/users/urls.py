from .views import *
from django.urls import include, path
urlpatterns = [
    path("register/", register, name="register"),
]

from django.urls import path, include
from .views import Index

app_name ='core'
urlpatterns = [
    path("", Index, name="index"),
]
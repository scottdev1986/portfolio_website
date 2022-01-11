from django.urls import path
from . import views

urlpatterns = [
    path('project/<slug:slug>', views.projects, name='projects'),
]
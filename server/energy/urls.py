from . import views
from django.urls import path

urlpatterns = [
    path(route="", view=views.home, name="energy-home"),
    path(route='upload/', view=views.upload, name="energy-upload"),
]

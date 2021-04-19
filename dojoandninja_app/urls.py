from django.urls import path
from . import views

urlpatterns =[
    path("",views.index),
    path("dojos/create",views.dojos_create),
    path("ninjas/create",views.ninjas_create),
    path("dojos/<int:dojos_id>/delete",views.dojos_delete)
]
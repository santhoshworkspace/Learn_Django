from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("new",views.new,name="new"),
    path("old_url",views.old_url,name="old_url"),
    path("new_url",views.new_url,name="new_url")
]
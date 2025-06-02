from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("",views.base,name="base"),
    path("post",views.detail,name="detail"),
    path("new",views.new,name="new_path"),
    path("old_url",views.old_url,name="old_url"),
    path("new_url",views.new_url,name="new_url_blog"),
    path("index",views.index,name="index"),
    path("*",views.all,name="All")
]
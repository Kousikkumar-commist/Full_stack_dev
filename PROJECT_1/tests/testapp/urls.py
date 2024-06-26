from django.contrib import admin
from django.urls import path

from . import views

admin.autodiscover()

urlpatterns = [

    path("admin/", admin.site.urls),
    path("change/", views.empty, name="change_book"),
    path("delete/", views.empty, name="delete_book"),
    path("raise/", views.empty, name="view_that_raises"),
    path("object/",views.empty, name="view_with_object"),
    path("list/",views.empty,name="view_with_permission_list"),

]

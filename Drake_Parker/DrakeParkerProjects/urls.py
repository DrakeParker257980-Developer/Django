from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="DrakeParkerProjects"),
    # path("DrakeForum/", views.DrakeForum, name="DrakeForum"),
    # path("DrakeChat/", views.DrakeChat, name="DrakeChat"),
    # path("AboutMe/", views.About, name="AboutMe"),
    # path("ProjectsMadeByDrakeParker/", views.About, name="Projects"),
    # path("ContactMe/", views.Contact, name="ContactMe"),
    # path("Search/", views.Search, name="Search"),
]
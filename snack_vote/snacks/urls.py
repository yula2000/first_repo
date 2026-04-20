from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_snack, name="add_snack"),
    path("vote/<int:snack_id>/", views.vote, name="vote"),
]

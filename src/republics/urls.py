from django.urls import path

from . import views
from .views import createrep

app_name = "republics"

urlpatterns = [
    path("", views.RepListView.as_view(), name="list"),
    path("detail/<slug:slug>/", views.RepDetailView.as_view(), name="detail")
]

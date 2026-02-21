from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("new/", views.category_create_view, name="create"),
]
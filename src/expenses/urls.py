from django.urls import path
from .views import expenses_list_view

app_name = "expenses"

urlpatterns = [
    path("", expenses_list_view, name="list")
]
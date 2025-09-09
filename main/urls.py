from django.urls import path
from .views import show_main   # import your view

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),  # homepage for the main app
]

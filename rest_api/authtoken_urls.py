from django.urls import re_path

from djoser import views

urlpatterns = [
    re_path(r"^login/?$", views.TokenCreateView.as_view(), name="login_api"),
    re_path(r"^logout/?$", views.TokenDestroyView.as_view(), name="logout_api"),
]
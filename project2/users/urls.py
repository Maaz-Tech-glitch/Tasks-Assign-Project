from django.urls import path
from . import views

urlpatterns = [
    path("",views.Login.as_view()),
    path("",views.RefreshTokenAPI.as_view()),
]

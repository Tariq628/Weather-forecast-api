
from django.urls import path
from . import views


urlpatterns = [
    path('data/', views.mater),
    path('<slug:slug>', views.ping),
]

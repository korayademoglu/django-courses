from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('kurslar',views.kurslar),
    path('hakkimizda',views.hakkimizda)
]

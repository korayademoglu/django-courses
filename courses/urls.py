from django.urls import path
from . import views

urlpatterns = [
    path('kurslar',views.kurslar),
    path('',views.test),
    path('youtube', views.youtubeLink),
    path('<cat>', views.getCoursesByCategory)
]

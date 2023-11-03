from django.urls import path
from . import views

urlpatterns = [
    path('kurslar',views.kurslar),
    path('<cat>', views.getCoursesByCategory)
]

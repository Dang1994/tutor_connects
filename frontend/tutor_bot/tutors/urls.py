from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_tutor, name='register_tutor'),
    path('search/', views.search_tutors, name='search_tutors'),
]

from django.urls import path
from .views import project, projects




urlpatterns = [
    path('projects/', projects),
    path('project/<str:pk>/', project),
]
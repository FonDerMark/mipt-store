from django.urls import path
from .views import Index, Api

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/', Api.as_view()),
]
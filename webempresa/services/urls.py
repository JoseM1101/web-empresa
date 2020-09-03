from django.urls import path
from . import views as sviews

urlpatterns = [

    path('services/',sviews.services,name='services'),
]

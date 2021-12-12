from django.urls import path
from . import views

urlpatterns = [
	path('', views.leap_year_view, name='leap-year')
]
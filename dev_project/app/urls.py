from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('find_person', views.find_person, name='find_person'),
    path('import_data', views.import_data, name='import_data'),
    ]
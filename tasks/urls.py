from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name = 'tasks'),
    path('create/', views.create_task, name= 'create'),
    path('edit/', views.edit_task, name= 'edit')
]
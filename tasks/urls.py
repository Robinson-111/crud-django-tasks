from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name = 'tasks'),
    path('create/', views.create_task, name= 'create'),
    path('<int:id>', views.details_task, name= 'detail'),
    path('<int:id>/edit/', views.edit_task, name= 'edit'),
    # path('<int:id>/edit', views.details_task, name= 'edit'),
    # path('<int:id/delete>', views.details_task, name= 'delete')
]
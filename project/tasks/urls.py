from django.urls import path
from .views import task_list, create_task, task_detail

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('task/<int:task_id>', task_detail, name='task_detail')
]
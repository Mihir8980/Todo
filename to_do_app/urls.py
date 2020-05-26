from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.home,name='home'),
    path('add_to_do/', views.add_to_do,name='add_to_do'),
    path('delete_to_do/<int:todo_id>/', views.delete_to_do,name='delete_to_do'),
    #path('imp/<int:i>/',views.imp,name="imp")
    path('todo-json/',views.todoList.as_view())
]
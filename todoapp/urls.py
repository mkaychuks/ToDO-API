from django.urls import path


from todoapp.views import (
    HomePageView, ListTodoView, CreateTodo, DeleteTodo,
    UpdateTodo, RetrieveTodo
) 


urlpatterns = [
    path('latest-todo/', HomePageView.as_view(), name='latest-todo'),
    path('todo/', ListTodoView.as_view(), name='personal-todo'),
    path('add-todo/', CreateTodo.as_view(), name='add-todo'),
    path('detail-todo/<int:pk>/', RetrieveTodo.as_view(), name='detail-todo'),
    path('update-todo/<int:pk>/', UpdateTodo.as_view(), name='update-todo'),
    path('delete-todo/<int:pk>/', DeleteTodo.as_view(), name='delete-todo'),
]
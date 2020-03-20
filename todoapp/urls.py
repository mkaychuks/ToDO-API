from django.urls import path


from todoapp.views import HomePageView, ListTodoView, CreateTodo


urlpatterns = [
    path('latest-todo/', HomePageView.as_view(), name='latest-todo'),
    path('todo/', ListTodoView.as_view(), name='personal-todo'),
    path('add-todo/', CreateTodo.as_view(), name='add-todo'),
]
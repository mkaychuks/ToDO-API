from django.urls import path


from todoapp.views import HomePageView


urlpatterns = [
    path('latest-todo/', HomePageView.as_view(), name='latest-todo'),
]
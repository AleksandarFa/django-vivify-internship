from django.urls import path, include
from .views import HomeView, UserView

urlpatterns = [
    path("todos/", HomeView.as_view()),
    path("users/", UserView.as_view()),
]
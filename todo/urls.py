from django.urls import path
from django.conf.urls import url
from .views import HomeView, UserView, UserViewSet, DetailTodoView
from rest_framework.routers import SimpleRouter

todo_urlpatterns = [
    path("todos/<int:pk>/", DetailTodoView.as_view()),
    path("todos/", HomeView.as_view()),
    path("users/<int:pk>/", UserViewSet.as_view({'get': 'retrieve'})),
    path("users/", UserView.as_view()),
    
]

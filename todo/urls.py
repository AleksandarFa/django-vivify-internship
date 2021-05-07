from django.urls import path
from django.conf.urls import url
from .views import HomeView, UserView, UserViewSet, DetailTodoView, PostTodoView, UpdateTodoView, DeleteTodoView
from rest_framework.routers import SimpleRouter

todo_urlpatterns = [
    path("todos/<int:pk>/", DetailTodoView.as_view()),
    path("todos/", HomeView.as_view()),
    path("users/<int:pk>/", UserViewSet.as_view({'get': 'retrieve'})),
    path("users/", UserView.as_view()),
    path("todos/post/", PostTodoView.as_view()),
    path("todos/update/<int:pk>/", UpdateTodoView.as_view({"put":"update", "patch":"partial_update"})),
    path("todos/delete/<int:pk>/", DeleteTodoView.as_view())
    
]

from django.urls import path
from django.conf.urls import url
from .views import HomeView, UserView, UserViewSet, DetailTodoView, PostTodoView, UpdateTodoView, DeleteTodoView, show_all_users_view, show_one_user
from rest_framework.routers import SimpleRouter

todo_urlpatterns = [
    path("todos/<int:pk>/", DetailTodoView.as_view()),
    path("todos/", HomeView.as_view()),
    path("users/<int:pk>/", show_one_user),
    path("users/", show_all_users_view),
    path("todos/post/", PostTodoView.as_view()),
    path("todos/update/<int:pk>/", UpdateTodoView.as_view({"put":"update", "patch":"partial_update"})),
    path("todos/delete/<int:pk>/", DeleteTodoView.as_view())
    
]

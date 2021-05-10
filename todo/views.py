from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Todo
from django.contrib.auth.models import User
from .serializers import UserSerializer, DetailTodoSerializer
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from django.views.generic.list import ListView
# Create your views here.

class HomeView(APIView):
    def get(self, request, format=None):
        todos = [todo.title for todo in Todo.objects.all()]
        return Response(todos)


class UserView(APIView):
    def get(self, request, format=None):
        users = [user.username for user in User.objects.all()]
        return Response(users)


class UserViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
        

class DetailTodoView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DetailTodoSerializer
    queryset = Todo.objects.all()


class PostTodoView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DetailTodoSerializer
    queryset = Todo.objects.all()


class UpdateTodoView(UpdateModelMixin, GenericViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DetailTodoSerializer
    queryset = Todo.objects.all()


class DeleteTodoView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DetailTodoSerializer
    queryset = Todo.objects.all()


def show_all_users_view(request):
    users = User.objects.all()
    context = {"users":users}
        
    return render(request, "users.html", context)


def show_one_user(request, pk=None):
    user = []
    if pk:
        user = User.objects.get(pk = pk)
    
    context = {"user":user}
    return render(request, "user.html", context)


        

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Todo
from django.contrib.auth.models import User
# Create your views here.

class HomeView(APIView):

    def get(self, request, format=None):
        todos = [todo.title for todo in Todo.objects.all()]
        return Response(todos)


class UserView(APIView):

    def get(self, request, format=None):
        users = [user.username for user in User.objects.all()]
        return Response(users)



        
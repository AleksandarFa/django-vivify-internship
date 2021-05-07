from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class DetailTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"



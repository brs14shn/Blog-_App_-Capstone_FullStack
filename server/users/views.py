
from django.contrib.auth.models import User
from .serializers import RegisterSerializers
from rest_framework import generics
from rest_framework.generics import CreateAPIView




class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializers


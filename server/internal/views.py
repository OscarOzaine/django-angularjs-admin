#from internal.models import Chain, Store, Employee
from internal.models import Snippet, RangeParameter
from internal.permissions import IsOwnerOrReadOnly, MyUserPermissions, AllowAll
#from internal.serializers import ChainSerializer, StoreSerializer, EmployeeSerializer, 
from internal.serializers import UserSerializer, SnippetSerializer, RangeParameterSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import authenticate
from django.db import connection


class AuthLogin(generics.ListAPIView):
    permission_classes = (AllowAll,)
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)

        user = authenticate(username=username, password=password)

        if user is not None:
            return Response(UserSerializer(request.user).data)
        else:
            return Response("-1")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class RangeParameterList(generics.ListCreateAPIView):
    serializer_class = RangeParameterSerializer

    def get_queryset(self):
        #user = self.request.user
        return RangeParameter.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RangeParameterDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	queryset = RangeParameter.objects.all()
	serializer_class = RangeParameterSerializer
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetList(generics.ListCreateAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (MyUserPermissions, )
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (MyUserPermissions, )
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


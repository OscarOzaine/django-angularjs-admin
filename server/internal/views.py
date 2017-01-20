from rest_framework import viewsets
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
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth import authenticate
import json

class AuthLogin(generics.ListAPIView):
    permission_classes = (AllowAll,)

    queryset = User.objects.none()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)

        print request.POST
        user = authenticate(username=username, password=password)
        #print user

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
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	queryset = RangeParameter.objects.all()
	serializer_class = RangeParameterSerializer
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class RangeParameterDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	queryset = RangeParameter.objects.all()
	serializer_class = RangeParameterSerializer
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

# class SnippetList(generics.ListCreateAPIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated,)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)
    
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
#     def perform_create(self, serializer):
#         serializer.save(owner = self.request.user)
#@require_http_methods(["GET", "POST"])
class SnippetList(generics.ListCreateAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (MyUserPermissions, )
    print 'test'
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



'''
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
'''
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# class User(viewsets.ModelViewSet):
#     """List all users or create a new User"""
#     def get_queryset(self):
#         return User.objects.all()

#     permission_classes = (permissions.IsAuthenticated,)
#     model = User
#     serializer_class = UserSerializer

    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class UserDetail(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class ChainViewSet(viewsets.ModelViewSet):
#     """ ViewSet for viewing and editing Chain objects """
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Chain.objects.all()
#     serializer_class = ChainSerializer


# class StoreViewSet(viewsets.ModelViewSet):
#     """ ViewSet for viewing and editing Store objects """
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer


# class EmployeeViewSet(viewsets.ModelViewSet):
#     """ ViewSet for viewing and editing Employee objects """
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

from django.shortcuts import render
from django.http import HttpResponse, Http404

from rest_framework import authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import CustomUser
from .serializers import FullCustomUserSerializer, BriefCustomUserSerializer




class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (permissions.AllowAny,)
 
    def post(self, request):
        user = request.data
        serializer = FullCustomUserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        pass


class TestAPI(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, format=None):
        return HttpResponse("Hello world!!")



class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    
    def get_object(self, email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        user = self.get_object(email)
        serializer = FullCustomUserSerializer(user)
        return Response(serializer.data)
"""
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

class UsersList(APIView): #Доделать
    """
    List of subscribers
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

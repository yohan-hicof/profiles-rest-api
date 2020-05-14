from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers
from profiles_api import models


class HelloApiView(APIView):
    """"Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """"Returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """"Create a hello message with the name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object from the DB"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test rest Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return an hello message"""
        a_viewset = [
            'User action (list, create, retrieve, update, partial_update and destroy)',
            'Automaticaly mpas to URLs using rooters',
            'Provide more functionality with less code',
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new set of entries in the DB"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'function': 'create', 'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrive a set of data from the DB"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Fully update a set of entries in the DB"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Patially update a set of entries in the DB"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destroy a set of entries in the DB"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

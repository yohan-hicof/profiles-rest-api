from rest_framework.views import APIView
from  rest_framework.response import Response


class HelloApiView(APIView):
    """"Test API view"""
    def get(self, request, format=None):
        """"Returns a list of APIview featurs"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})

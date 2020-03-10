from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
from rest_framework import viewsets

class HelloApiView(APIView):
    """ Testing api view response """

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of api views """
        
        an_apiview = [
            'is used to get response using HTTP function (get, post, put, patch, delete)',
            'is similar to the traditional Django view',
            'is manually mapped to Urls',
        ]
        
        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        })
    
    def post(self, request):
        """ create a hello message with our name """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating of an object """
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Handle partial updating of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test view set """

    serializer_class = HelloSerializer

    def list(self, request):
        """ Return message with name """
        a_viewset = [
            'Automatically maps to URLS by Routers',
            'More functionality with less code'
        ]

        return Response({
            'message': 'Hello',
            'a_viewset': a_viewset
        })
    
    def create(self, request, pk=None):
        """ Creating an object """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Retrive an object by its ID """
        return Response({'method': 'RETRIEVE'})

    def partial_update(self, request, pk=None):
        """ Update object partially """
        return Response({'method': 'PARTIAL_UPDATE'})
    
    def destroy(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})

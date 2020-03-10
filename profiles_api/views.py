from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer

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

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Testing api view response """

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
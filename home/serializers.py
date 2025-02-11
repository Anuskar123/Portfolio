from rest_framework import serializers
from rest_framework import api_view
from rest_framework import response
from rest_framework import status

@api_view(['GET'])
def api_List(request):
    return api_view({'message': 'Hello, world!'})
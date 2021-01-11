from django.shortcuts import render
from rest_framework.decorators import api_view
from users.models import User
from users.serializers import UserSerializer

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
from django.contrib.auth import authenticate, login
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authtoken.models import Token
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_200_OK)
from .schemas import RegistrationSchema
from .forms import RegistrationForm
from rest_framework.permissions import IsAuthenticated


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties=RegistrationSchema().__dict__,
    description='kjhgfd'
))
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def registration(request):
    # token - ը ոնց փոխանցեմ
    # աշխատի միայն այն դեպքում երբ login է եղել admin-ը
    # ամբողջ սխալը գալիս է settings.py-ից
    print('register user', request.user.is_superuser)
    if request.user.is_superuser:
        form = RegistrationForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'msg': 'ok'}, status=HTTP_200_OK)
        else:

            return Response({'errors': form.errors}, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({'errors': 'Only admin can register a user'})


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='string', default=''),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='string', default=''),
    }
))
@api_view(['POST'])
def login(request):
    # print('request', request)
    username = request.data['username']
    password = request.data['password']
    if not username or not password or username is None or password is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(request, username=username, password=password)
    # print('user', user)
    if not user:
        return Response({'error': 'Invalid Credentials'})
    token, _ = Token.objects.get_or_create(user=user)
    # print('user=======>', request.user)
    return Response({'token': token.key})

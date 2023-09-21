from django.contrib.auth import authenticate, login
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authtoken.models import Token
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_200_OK)
from .schemas import RegistrationSchema, CourseSchema, GroupSchema, ModuleSchema
from .forms import RegistrationForm, ModuleForm, CourseForm, GroupForm
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, CustomUserSerializer
from .models import CustomUser


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties=RegistrationSchema().__dict__,
    # description='kjhgfd'
))
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def registration(request):
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
    username = request.data['username']
    password = request.data['password']
    if not username or not password or username is None or password is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'})
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getProfile(request):
    user = CustomUserSerializer(CustomUser.objects.get(user_ptr_id=request.user.id)).data
    return Response({'user': user})


# --------------------------- create --------------------------------------
@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties=CourseSchema().__dict__,
))
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def createCourse(request):
    form = CourseForm(request.data)
    if form.is_valid():
        form.save()
        return Response({'msg': 'ok'}, status=HTTP_200_OK)
    else:
        return Response({'errors': form.errors})


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties=ModuleSchema().__dict__,
))
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def createModule(request):
    return Response({})


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties=GroupSchema().__dict__,
))
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def createGroup(request):
    return Response({})


# ---------------------------------------- get ---------------------------------
# 1 - manage | 2 - teacher | 3 - student

@api_view(['GET'])
def getManagers(request):
    data = CustomUser.objects.filter(status='1')
    managers = list(map(lambda a: CustomUserSerializer(CustomUser.objects.get(user_ptr_id=a.id)).data, data))
    return Response({'managers': managers})


@api_view(['GET'])
def getTeachers(request):
    data = CustomUser.objects.filter(status='2')
    teachers = list(map(lambda a: CustomUserSerializer(CustomUser.objects.get(user_ptr_id=a.id)).data, data))
    return Response({'teachers': teachers})


@api_view(['GET'])
def getStudents(request):
    data = CustomUser.objects.filter(status='3')
    students = list(map(lambda a: CustomUserSerializer(CustomUser.objects.get(user_ptr_id=a.id)).data, data))
    return Response({'students': students})


@api_view(['PUT'])
def settingsAdmin(request):
    return Response({})


@api_view(['PUT'])
def settingsUser(request):
    return Response({})


@api_view(['PUT'])
def changeData(request):
    return Response({})


@api_view(['PUT'])
def changeStatus(request):
    return Response({})


@api_view(['DELETE'])
def deleteUser(request):
    return Response({})


# ? - հարցման տեսակը
@api_view(['POST'])
def changeCourse(request):
    return Response({})


@api_view(['POST'])
def changeModule(request):
    return Response({})


@api_view(['POST'])
def changeGroup(request):
    return Response({})


@api_view(['POST'])
def changeGroupModule(request):
    return Response({})


@api_view(['GET'])
def getAllCourse(request):
    return Response({})


@api_view(['GET'])
def getModuleByCourseId(request):
    return Response({})


@api_view(['GET'])
def getAllGroup(request):
    return Response({})


@api_view(['GET'])
def getGroupsByTeacherId(request):
    return Response({})


@api_view(['POST'])
def addStudentInGroup(request):
    return Response({})


@api_view(['DELETE'])
def deleteStudentGroup(request):
    return Response({})


@api_view(['POST'])
def changeStudentGroup(request):
    return Response({})


@api_view(['GET'])
def getGroupById(request):
    return Response({})


@api_view(['POST'])
def addStudent(request):
    return Response({})

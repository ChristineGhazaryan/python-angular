from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('registration', views.registration),
    path('getProfile', views.getProfile),
    # path('createGroup', views.createGroup),
    path('createCourse', views.createCourse),
    # path('createModule', views.createModule),
    path('getManagers', views.getManagers),
    path('getStudents', views.getStudents),
    path('getTeachers', views.getTeachers),
    # path('getAllGroup', views.getAllGroup),
    # path('getAllCourse', views.getAllCourse),
    # path('getGroupById/<int:id>', views.getGroupById),
    # path('getGroupsByTeacherId/<int:id>', views.getGroupsByTeacherId),
    # path('getModuleByCourseId/<int:id>', views.getModuleByCourseId),
]

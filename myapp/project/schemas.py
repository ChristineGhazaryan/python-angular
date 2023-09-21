from drf_yasg import openapi


class RegistrationSchema:
    def __init__(self, *args, **kwargs):
        self.first_name = openapi.Schema(type=openapi.TYPE_STRING, description='', default='')
        self.last_name = openapi.Schema(type=openapi.TYPE_STRING, description='', default='')
        self.email = openapi.Schema(type=openapi.TYPE_STRING, description='', default='')
        self.username = openapi.Schema(type=openapi.TYPE_STRING, description='', default='')
        self.password1 = openapi.Schema(type=openapi.TYPE_STRING, default='')
        self.password2 = openapi.Schema(type=openapi.TYPE_STRING, default='')
        self.status = openapi.Schema(type=openapi.TYPE_STRING, default='')


class CourseSchema:
    def __init__(self):
        self.name = openapi.Schema(type=openapi.TYPE_STRING, description='', default='')


class ModuleSchema:
    def __init__(self):
        self.name = openapi.Schema(type=openapi.TYPE_STRING, description='', default='')
        self.course_id = openapi.Schema(type=openapi.TYPE_INTEGER, description='', default='')


class GroupSchema:
    def __init__(self):
        self.name = openapi.Schema(type=openapi.TYPE_STRING, description='', default='')
        self.course_id = openapi.Schema(type=openapi.TYPE_INTEGER, description='', default='')
        self.module_id = openapi.Schema(type=openapi.TYPE_INTEGER, description='', default='')
        self.teacher_id = openapi.Schema(type=openapi.TYPE_INTEGER, description='', default='')

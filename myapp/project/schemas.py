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

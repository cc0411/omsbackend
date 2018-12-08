from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets,mixins
from .serializer import  UserInfoSerializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.permissions import IsAuthenticated
User = get_user_model()
# Create your views here.
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
class CustomBackend(ModelBackend):
    def authenticate(self, request,username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class  UserInfoViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = UserInfoSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    #lookup_field = "username"
    def get_object(self):
        return self.request.user


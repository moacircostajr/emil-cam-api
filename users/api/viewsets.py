from django.contrib.auth import hashers
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import User

from users.api.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        username = self.request.user  # fazer a busca pelo token ?
        queryset = User.objects.filter(username__exact=username)
        company = queryset[0].id_company
        return User.objects.filter(id_company=company)

    def create(self, request, *args, **kwargs):
        raw_password = request.data['password']
        request.data['password'] = hashers.make_password(raw_password)
        return super(UsersViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request):
        return Response(status=status.HTTP_403_FORBIDDEN)


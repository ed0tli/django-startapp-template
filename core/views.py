from rest_framework import viewsets, status, generics

from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        # NOTE: filter out anonymous user and administrator
        return CustomUser.objects.filter(pk__gt=1)

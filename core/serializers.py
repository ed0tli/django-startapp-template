from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        return obj.get_avatar()

    class Meta:
        model = CustomUser
        exclude = ('password', )

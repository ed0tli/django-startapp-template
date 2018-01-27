from django.conf.urls import include, url

from rest_framework import routers

from core.views import CustomUserViewSet

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'user', CustomUserViewSet, base_name='user')

urlpatterns = [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    ] + router.urls

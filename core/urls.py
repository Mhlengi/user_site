from django.contrib.auth import get_user_model
from django.urls import path, include
from rest_framework import routers

from core.views_api import UserViewSet

User = get_user_model()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import viewsets, renderers, parsers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        email = request.data['email'] if 'email' in request.data else None
        password = request.data['password'] if 'password' in request.data else None

        user = authenticate(email=email, password=password)
        if user is None or user.is_anonymous:
            return Response({'token': ''}, status=status.HTTP_401_UNAUTHORIZED)

        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

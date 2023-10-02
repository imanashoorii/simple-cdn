from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.permissions import UserIsOwnerOrReadOnly
from accounts.serializers import UserSerializer, CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserRegisterAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserInfoAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, UserIsOwnerOrReadOnly)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UpdateUserInfo(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserIsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

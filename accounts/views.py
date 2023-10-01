from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import UserIsOwnerOrReadOnly
from accounts.serializers import UserSerializer


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

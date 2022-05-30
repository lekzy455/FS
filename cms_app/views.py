from django.shortcuts import render
from .models import Announcement, UserGroup, WorkerGroup, Comment
from django.contrib.auth import get_user_model
from .serializers import AnnouncementSerializer, GroupSerializer, GroupSignupSerializer, CommentSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

User = get_user_model() 

class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

class GroupList(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

class GroupSignUp(generics.CreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = GroupSignupSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Comment(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    



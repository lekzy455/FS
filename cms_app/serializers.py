from rest_framework import serializers
from .models import Announcement, WorkerGroup, UserGroup, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerGroup
        fields = ("name", )

class GroupSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"
        read_only_fields = ['user_id']

class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class meta:
        model = Comment
        fields = "__all__"


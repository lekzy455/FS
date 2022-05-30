from django.urls import path
from .views import (
    AnnouncementList,
    GroupList,
    GroupSignUp,
    UserList,
    UserDetail,
    UserUpdate,
    Comment,
)

urlpatterns = [
    path('announcement/', AnnouncementList.as_view(), name="announcement"),
    path('groups/', GroupList.as_view(), name="groups"),
    path('join-group/', GroupSignUp.as_view(), name="join-group"),
    path('users/', UserList.as_view(), name="users"),
    path('users/<str:username>/', UserDetail.as_view(), name="user-detail"),
    path('users/<str:username>/update/', UserUpdate.as_view(), name="user-update"),
    path('comments/', Comment.as_view(), name="comments"),
]
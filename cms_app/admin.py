from django.contrib import admin
from .models import (
    User, Role, UserRole, WorkerGroup, UserGroup, Attendances, Testimony, Comment, Review, 
    Announcement
)

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(WorkerGroup)
admin.site.register(UserGroup)
admin.site.register(Attendances)
admin.site.register(Testimony)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Announcement)
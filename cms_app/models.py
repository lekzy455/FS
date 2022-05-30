from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_id = models.CharField(max_length=20, blank=True, null=True)
    facebook_id = models.CharField(max_length=45, blank=True, null=True)
    instagram_id = models.CharField(max_length=45, blank=True, null=True)
    twitter_id = models.CharField(max_length=45, blank=True, null=True)
    date_of_birth= models.DateField(blank=True, null=True)
    salt = models.CharField(max_length=100, blank=True, null=True)
    reset_password = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    locked = models.IntegerField(blank=True, null=True)
    last_check_in = models.DateTimeField(blank=True, null=True)
    last_password_change = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Users"

class Role(models.Model):
    name = models.CharField(max_length=45)
    active = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Roles"

class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "UserRoles"

class WorkerGroup(models.Model):
    name = models.CharField(max_length=45)
    active = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "WorkerGroups"

class UserGroup(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(WorkerGroup, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "UserGroups"

class Attendances(models.Model):
    date = models.DateTimeField(auto_now_add=False, auto_now=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Attendances"

class Testimony(models.Model):
    title = models.CharField(max_length=200)
    testimony = models.TextField()
    status = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Testimonies"


class Comment(models.Model):
    comments = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Comments"

class Review(models.Model):
    feedback = models.TextField()
    review = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Reviews"

class Announcement(models.Model):
    announcements = models.TextField()
    send_to = models.IntegerField()
    status = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.CharField(max_length=45)

    class Meta:
        ordering = ["-last_modified_date"]
        verbose_name_plural = "Accouncements"







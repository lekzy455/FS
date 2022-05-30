from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {'password': {'write_only':True}}

    def validate_email(self, data):
        email = data
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise serializers.ValidationError("Email already exists")
        return data

    def validate_username(self, data):
        username = data
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise serializers.ValidationError("Username already exists")
        return data
    
    def validate_password(self, data):
        password = data
        if len(password) < 8:
            raise serializers.ValidationError("password must have a minimum length of 8 characters")
        elif not re.findall('\d', password):
            raise serializers.ValidationError("password must contain at least 1 digit, 0-9.")
        elif not re.findall('[A-Z]', password):
            raise serializers.ValidationError("password must contain at least 1 uppercase letter, A-Z.")
        elif not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise serializers.ValidationError("The password must contain at least 1 special character: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?")
        return data
    
    def validate(self, data):
        password = data.get('password')
        password2 = data.pop('password2')
        if password2 != password:
            raise serializers.ValidationError("Passwords mismatch")
        return data
    
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.is_active = False
        user.save()
        return user



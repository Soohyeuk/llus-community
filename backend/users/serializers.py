from django.contrib.auth import get_user_model
from rest_framework import serializers # To create serializers
from .models import User # Custom user model from models.py
from django.contrib.auth import authenticate # Verify username and email and password



User = get_user_model()

class UserSerializer(serializers.ModelSerializer): # This serializer translates between the user model instances and JSON representation
    #mdoelserializer automatically creates serilzation fields based on your model fields
    class Meta: 
        model = User # Links serializer directly to your custom user model
        fields = [ # Allowed for serialization and desrialization 
            'id', 'username', 'email', 'first_name', 'last_name', 'us_phone_number',
            'gender', 'birth_date', 'grad_date', 'role', 'created_at', 'major', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}} # Provides extra settings (here, password will only be accepted when creating/updating users but never sent back.)

    def validate_username(self, value):
        """ Ensure username is unique """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        """ Ensure email is unique """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value
    
    def validate_us_phone_number(self, value):
        if User.objects.filter(us_phone_number=value).exists():
            raise serializers.ValidationError("The phone number already exist")
        return value

    def create(self, validated_data):
        """ Creates user with hashed password. """
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user



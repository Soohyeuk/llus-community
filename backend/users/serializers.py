from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'english_name', 'us_phone_number',
            'gender', 'birth_date', 'school', 'grad_date', 'role', 'created_at', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """ Validates the role of the user when creating a user """
        role = data.get('role')

        if role == 'user': 
            required_fields = ['school', 'grad_date']
            forbidden_fields = []
        elif role == 'admin': 
            required_fields = []
            forbidden_fields = ['school', 'grad_date']
        else:
            raise serializers.ValidationError("Invalid role.")
        
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f"{field} is required for {role}."})

        for field in forbidden_fields:
            if data.get(field):
                raise serializers.ValidationError({field: f"{field} is not allowed for {role}."})

        return data

    def create(self, validated_data):
        """ Creates user with hashed password. """
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        data['user'] = user
        return data

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model 
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Ensure password is write-only and use CharField for handling passwords
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user using the custom user model
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''), 
            profile_picture=validated_data.get('profile_picture', None)
        )

        # Create an authentication token for the new user
        Token.objects.create(user=user)

        return user

# ["serializers.CharField()", "get_user_model().objects.create_user"]
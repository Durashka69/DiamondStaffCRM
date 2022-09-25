from rest_framework import serializers

from profiles.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_staff'
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        read_only=True
    )

    class Meta:
        model = Profile
        fields = (
            'user',
            'profile_photo'
        )

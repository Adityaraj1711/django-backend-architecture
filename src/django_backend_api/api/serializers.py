from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class SkillSerializer(serializers.ModelSerializer):
    """A serializer for skill set and its rating."""

    class Meta:
        model = models.Skill
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class CollegeSerializer(serializers.ModelSerializer):
    """A serializer for college details."""

    class Meta:
        model = models.College
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class AboutSerializer(serializers.ModelSerializer):
    """A serializer for about section."""

    class Meta:
        model = models.About
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class CompanySerializer(serializers.ModelSerializer):
    """A serializer for work experience or company model."""

    class Meta:
        model = models.Company
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class ProjectSerializer(serializers.ModelSerializer):
    """A serializer for project model details."""

    class Meta:
        model = models.Project
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class InterestSerializer(serializers.ModelSerializer):
    """A serializer for interest model."""

    class Meta:
        model = models.Interest
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class AchievementSerializer(serializers.ModelSerializer):
    """A serializer for achievements."""

    class Meta:
        model = models.Achievement
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class CertificationSerializer(serializers.ModelSerializer):
    """A serializer for certificate details."""

    class Meta:
        model = models.Certification
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for portfolio feed items."""

    class Meta:
        model = models.Portfolio
        fields = ('url', 'name', 'created_on', 'email', 'skill', 'work_experience', 'about', 'achievement', 'interest',
                  'certification', 'project', 'education')
        extra_kwargs = {'user_profile': {'read_only': True}}
        depth = 1


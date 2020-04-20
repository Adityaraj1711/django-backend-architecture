from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework import generics
from . import serializers
from . import models
from . import permission


class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'del'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user_profile=self.request.user)


class PortfolioViewSet(generics.ListAPIView):
    """Handles reading portfolios for all the users by username """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.PortfolioSerializer
    queryset = models.Portfolio.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        if len(models.Portfolio.objects.filter(user_profile__name=self.kwargs['username'])) > 0:
            id = models.Portfolio.objects.filter(user_profile__name=self.kwargs['username']).last().id
            return self.queryset.filter(user_profile__name=self.kwargs['username'], id=id)
        return self.queryset.filter(user_profile__name=self.kwargs['username'])

    def list(self, request, *args, **kwargs):
        """ appends the status of request """
        queryset = self.filter_queryset(self.get_queryset())
        summary = {'details_count': queryset.filter(user_profile__name=self.kwargs['username']).count()}

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {'summary': summary, 'data': serializer.data}
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = {'summary': summary, 'data': serializer.data}
        return Response(data)


class PortfolioDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PostPortfolioDetailsViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating portfolio details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.PortfolioSerializer
    queryset = models.Portfolio.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        return self.queryset.filter(user_profile=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_profile=self.request.user)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        if (len(models.Portfolio.objects.filter(user_profile__id=self.request.user.id))) == 0:
            serializer.save(user_profile=self.request.user)
        else:
            raise Exception('Multiple objects is created')


class SkillViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating skill set for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.SkillSerializer
    queryset = models.Skill.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        skill_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.skill.add(skill_obj)
        portfolio_obj.save()


class CollegeViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating college details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CollegeSerializer
    queryset = models.College.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        college_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.education.add(college_obj)
        portfolio_obj.save()


class CompanyViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating college details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        company_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.work_experience.add(company_obj)
        portfolio_obj.save()


class ProjectViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating college details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        project_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.project.add(project_obj)
        portfolio_obj.save()


class InterestViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating college details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.InterestSerializer
    queryset = models.Interest.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        interest_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.interest.add(interest_obj)
        portfolio_obj.save()


class AchievementViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating college details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.AchievementSerializer
    queryset = models.Achievement.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        achievement_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.achievement.add(achievement_obj)
        portfolio_obj.save()


class CertificationViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating college details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CertificationSerializer
    queryset = models.Certification.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        certification_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.certification.add(certification_obj)
        portfolio_obj.save()


class AboutViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating college details for logged in users."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.AboutSerializer
    queryset = models.About.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user_profile=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        about_obj = serializer.save(user_profile=self.request.user)
        portfolio_obj = models.Portfolio.objects.get(user_profile__id=self.request.user.id)
        portfolio_obj.about.add(about_obj)
        portfolio_obj.save()

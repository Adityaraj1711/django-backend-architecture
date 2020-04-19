from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, 'login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('college', views.CollegeViewSet)
router.register('college', views.CompanyViewSet)
router.register('college', views.ProjectViewSet)
router.register('college', views.InterestViewSet)
router.register('skill', views.SkillViewSet)
router.register('college', views.AchievementViewSet)
router.register('college', views.CertificationViewSet)

# router.register('<int:pk>', views.PortfolioViewSet)
router.register('portfolio-update', views.PostPortfolioDetailsViewSet)

urlpatterns = [
    url(r'^hello-view/<username>', views.HelloApiView.as_view()),
    path("user/<username>", views.PortfolioViewSet.as_view(), name="portfolio_list"),
    path("user/<username>/<int:pk>", views.PortfolioDetailViewSet.as_view(), name="portfolio_detail"),
    url(r'', include(router.urls)),
]

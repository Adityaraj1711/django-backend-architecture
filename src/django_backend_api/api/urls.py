from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello-viewset')
router.register('signup', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, 'login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('education', views.CollegeViewSet)
router.register('work-experience', views.CompanyViewSet)
router.register('projects', views.ProjectViewSet)
router.register('interests', views.InterestViewSet)
router.register('skills', views.SkillViewSet)
router.register('achievements', views.AchievementViewSet)
router.register('certificates', views.CertificationViewSet)
router.register('about', views.AboutViewSet)
router.register('portfolio-update', views.PostPortfolioDetailsViewSet)

urlpatterns = [
    url(r'^hello-view/<username>', views.HelloApiView.as_view()),
    path("user/<username>", views.PortfolioViewSet.as_view(), name="portfolio_list"),
    path("user/<username>/<int:pk>", views.PortfolioDetailViewSet.as_view(), name="portfolio_detail"),
    url(r'', include(router.urls)),
]

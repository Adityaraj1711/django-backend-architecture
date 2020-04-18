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
# router.register('<int:pk>', views.PortfolioViewSet)

urlpatterns = [
    url(r'^hello-view/<username>', views.HelloApiView.as_view()),
    path("user/<username>", views.PortfolioViewSet.as_view(), name="portfolio_list"),
    url(r'', include(router.urls)),
]

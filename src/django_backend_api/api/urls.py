from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^hello-world/', views.HelloApiView.as_view()),
]

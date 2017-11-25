from django.conf.urls import url
from Vue import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),# Notice the URL has been named
]
from django.conf.urls import url
from articles import views


urlpatterns = [
    url(r'^home/$', views.main, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail')]
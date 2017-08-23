from django.conf.urls import url
from articles import views


urlpatterns = [
    url(r'^home/$', views.home,)
]
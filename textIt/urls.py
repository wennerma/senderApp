from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send_text$', views.send_text, name='send_text'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login_user', views.login_user, name='login_user'),
]
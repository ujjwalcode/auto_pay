from django.conf.urls import url
from . import views

app_name = 'pay'

urlpatterns = [
    url(r'^logout_user/$', views.logout_user, name = 'logout_user'),
    url(r'^login_user/$', views.login_user, name = 'login_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, name = 'index'),
    url(r'^bank_detail/$', views.bank_detail, name = 'bank_detail'),
    url(r'^gateway/$', views.gateway, name = 'gateway'),
]

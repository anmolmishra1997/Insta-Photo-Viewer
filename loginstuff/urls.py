from django.conf.urls import url

from . import views

app_name = 'loginstuff'
urlpatterns = [
    # ex: /loginstuff/
    url(r'^instalogin/$', views.queryForToken, name='index'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^constitution/$', views.constitution),
    url(r'^events/$', views.events),
    url(r'^index/$', views.index),
    url(r'^showcase/$', views.showcase),
    url(r'^industry/$', views.industry),
    url(r'^join/$', views.join),
    url(r'^resources/$', views.resources),
    url(r'^hackathon13/$', views.hackathon13),
    url(r'^hackathon14/$', views.hackathon14),
    url(r'^hackathonsp15/$', views.hackathonsp15),
    url(r'^hackathonfa15/$', views.hackathonfa15),
    url(r'^hackathonsp16/$', views.hackathonsp16),
    url(r'^hackathonfa16/$', views.hackathonfa16),
]
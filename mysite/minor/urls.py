from django.conf.urls import include,url
from django.contrib import admin

from . import views
#superuser--user,pass1234  kandy password1125
urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^regmech/$', views.regmech , name='regmech'),
    url(r'^regrider/$', views.regrider , name='regrider'),
    url(r'^reqmech/$', views.reqmech , name='reqmech'),
    url(r'^chkreq/$', views.chkreq , name='chkreq'),
    url(r'^postdata/$', views.postdata , name='postdaata'),
    url(r'^loginusr/$', views.loginusr , name='loginusr'),
    url(r'^loginmech/$', views.loginmech , name='loginmech'),
    url(r'^findmech/$', views.findmech , name='findmech'),
    #url(r'^img/$', include('img.urls')),
    #url(r'^admin/', include(admin.site.urls)),
]

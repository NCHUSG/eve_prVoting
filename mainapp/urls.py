from django.conf.urls import patterns, url, include
from mainapp import views                                                                                                                   

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^submit/', views.Submit, name='submit')
)

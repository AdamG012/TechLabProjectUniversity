from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.trends_index, name='trends_index'),
    url(r'^trend/([0-9]+)$', views.trend_page, name='trend_page'),
    url(r'^project/([0-9]+)$', views.project_page, name='project_page'),
    url(r'^principles/$', views.principles_page, name='principles_page'),
    url(r'^icttechlab/$', views.icttechlab_page, name='icttechlab_page'),
    url(r'^search-results/([[\w]*[\s]*]*)$', views.search_page, name='search_page'),
]

from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('search', views.search, name='search'),
    path(r'^articles/(?P<article_id>[0-9]+)/$', views.article, name='article')
]
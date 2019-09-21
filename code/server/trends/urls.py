from django.urls import path


from . import views

urlpatterns = [
    path('search', views.search, name='search'),
    path(r'^articles/(?P<article_id>[0-9]+)/$', views.article, name='article'),
    path('latest-articles', views.latest_articles, name='latest-articles'),
    path('abstract', views.article_abstract, name='abstract'),
]

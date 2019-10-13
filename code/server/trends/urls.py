from django.urls import path
from trends import views, admin_views

urlpatterns = [
    path('search', views.search, name='search'),
    path('articles/<int:article_id>', views.article_data, name='article'),
    path('latest-articles', views.latest_articles, name='latest-articles'),
    path('abstract', views.article_abstract, name='abstract'),
    path('admin/article-new', admin_views.article_new, name='article-new'),
    path('admin/article-edit', admin_views.article_edit, name='article-edit'),
    path('admin/article-remove', admin_views.article_remove, name='article-remove'),
    path('admin/login', admin_views.login, name='login'),
    path('admin/logout', admin_views.logout, name='logout'),
]
